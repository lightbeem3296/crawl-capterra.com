import argparse
import ctypes
import json
import os
import time
import traceback
from datetime import datetime
from pathlib import Path
from random import randint
from typing import Optional

import requests
import urllib3
from bs4 import BeautifulSoup

from libchrome import Chrome
from liblogger import log_err, log_inf

urllib3.disable_warnings()

COOKIE = ""
USER_AGENT = ""

CUR_DIR = str(Path(__file__).parent.absolute())
TEMP_DIR = os.path.join(CUR_DIR, "temp")
OUTPUT_DIR = os.path.join(CUR_DIR, "output")
DONE_MARKER_NAME = "done"


CHROME = None

BASE_URL = "https://www.capterra.com"
COOKIE_DOMAIN = ".capterra.com"
PAGE_SIZE = 25


CATEGORY_LIST = [
    "0. 360 Degree Feedback > /360-degree-feedback-software/",
    "1. 3D Architecture > /3d-architecture-software/",
    "2. 3D CAD > /3d-cad-software/",
    "3. 3D Rendering > /3d-rendering-software/",
    "4. AB Testing > /ab-testing-software/",
    "5. Absence Management > /absence-management-software/",
    "6. Access Governance > /access-governance-software/",
    "7. Account Based Marketing > /account-based-marketing-software/",
    "8. Accounting > /accounting-software/",
    "9. Accounting Practice Management > /accounting-practice-management-software/",
    "10. Accounts Payable > /accounts-payable-software/",
    "11. Accounts Receivable > /accounts-receivable-software/",
    "12. Accreditation Management > /accreditation-management-software/",
    "13. Ad Server > /ad-server-software/",
    "14. Address Verification > /address-verification-software/",
    "15. Admissions > /admissions-software/",
    "16. Advanced Planning and Scheduling (APS) > /aps-software/",
    "17. Advertising Agency > /advertising-agency-software/",
    "18. Advocacy > /advocacy-software/",
    "19. Aerospace Manufacturing > /aerospace-manufacturing-software/",
    "20. Affiliate > /affiliate-software/",
    "21. Agile Project Management > /agile-project-management-tools-software/",
    "22. AI Code Generator > /ai-code-generator-software/",
    "23. AI Image Generator > /ai-image-generator-software/",
    "24. AI Marketing Tools > /ai-marketing-tools-software/",
    "25. AI Sales Assistant > /ai-sales-assistant-software/",
    "26. AI Video Generator > /ai-video-generator-software/",
    "27. AI Writing Assistant > /ai-writing-assistant-software/",
    "28. AIOps Platforms > /aiops-platforms-software/",
    "29. Airline Reservation System > /airline-reservation-system-software/",
    "30. All-in-One Marketing Platform > /all-in-one-marketing-software/",
    "31. Alumni Management > /alumni-management-software/",
    "32. AML > /aml-software/",
    "33. Android Kiosk > /android-kiosk-software/",
    "34. Animal Shelter > /animal-shelter-software/",
    "35. Animation > /animation-software/",
    "36. Anti-spam > /anti-spam-software/",
    "37. AntiVirus > /anti-virus-software/",
    "38. Apartment Management Systems > /apartment-management-software/",
    "39. API Management > /api-management-software/",
    "40. App Building > /app-building-software/",
    "41. App Design > /app-design-software/",
    "42. App Store Optimization Tools > /app-store-optimization-tools-software/",
    "43. Apparel Management > /apparel-management-software/",
    "44. Applicant Tracking > /applicant-tracking-software/",
    "45. Application Development > /application-development-software/",
    "46. Application Lifecycle Management > /application-lifecycle-management-software/",
    "47. Application Performance Management > /application-performance-management-software/",
    "48. Applied Behavior Analysis > /applied-behavior-analysis-software/",
    "49. Appointment Reminder > /appointment-reminder-software/",
    "50. Appointment Scheduling > /appointment-scheduling-software/",
    "51. Arborist > /arborist-software/",
    "52. Architectural CAD > /architectural-cad-software/",
    "53. Architecture > /architecture-software/",
    "54. Archiving > /archiving-software/",
    "55. Art Gallery > /art-gallery-software/",
    "56. Artificial Intelligence > /artificial-intelligence-software/",
    "57. Assessment > /assessment-software/",
    "58. Asset Tracking > /asset-tracking-software/",
    "59. Assisted Living > /assisted-living-software/",
    "60. Association Management > /association-management-software/",
    "61. Attendance Tracking > /attendance-tracking-software/",
    "62. Auction > /auction-software/",
    "63. Audience Response > /audience-response-software/",
    "64. Audio Conferencing > /audio-conferencing-software/",
    "65. Audio Editing > /audio-editing-software/",
    "66. Audit > /audit-software/",
    "67. Augmented Reality > /augmented-reality-software/",
    "68. Authentication > /authentication-software/",
    "69. Auto Body > /auto-body-software/",
    "70. Auto Dealer > /auto-dealer-software/",
    "71. Auto Dealer Accounting > /auto-dealer-accounting-software/",
    "72. Auto Dialer > /auto-dialer-software/",
    "73. Auto Repair > /auto-repair-software/",
    "74. Automated Testing > /automated-testing-software/",
    "75. Aviation Maintenance > /aviation-maintenance-software/",
    "76. B2B eCommerce Platform > /b2b-ecommerce-platform-software/",
    "77. Background Check > /background-check-software/",
    "78. Backup > /backup-software/",
    "79. Bakery > /bakery-software/",
    "80. Banking Systems > /banking-systems-software/",
    "81. Bankruptcy > /bankruptcy-software/",
    "82. Bar POS > /bar-pos-software/",
    "83. Barbershop > /barbershop-software/",
    "84. Barcoding > /barcoding-software/",
    "85. Benefits Administration > /benefits-administration-software/",
    "86. Big Data > /big-data-software/",
    "87. Bill of Materials > /bill-of-materials-software/",
    "88. Billing and Invoicing > /billing-and-invoicing-software/",
    "89. Billing and Provisioning > /billing-and-provisioning-software/",
    "90. BIM > /bim-software/",
    "91. Blockchain Platforms > /blockchain-platforms-software/",
    "92. Blog > /blog-software/",
    "93. Board Management > /board-management-software/",
    "94. Bookkeeper > /bookkeeper-software/",
    "95. Bot Detection and Mitigation > /bot-detection-and-mitigation-software/",
    "96. Brand Management > /brand-management-software/",
    "97. Brand Protection > /brand-protection-software/",
    "98. Brewery > /brewery-software/",
    "99. Brokerage Management > /brokerage-management-software/",
    "100. Browser > /browser-software/",
    "101. Budgeting > /budgeting-software/",
    "102. Bug Tracking > /bug-tracking-software/",
    "103. Building Maintenance > /building-maintenance-software/",
    "104. Business Card > /business-card-software/",
    "105. Business Continuity > /business-continuity-software/",
    "106. Business Intelligence > /business-intelligence-software/",
    "107. Business Management > /business-management-software/",
    "108. Business Performance Management > /business-performance-management-software/",
    "109. Business Phone Systems > /business-phone-systems-software/",
    "110. Business Plan > /business-plan-software/",
    "111. Business Process Management > /business-process-management-software/",
    "112. Buyer Intent > /buyer-intent-software/",
    "113. Calendar > /calendar-software/",
    "114. Calibration Management > /calibration-management-software/",
    "115. Call Accounting > /call-accounting-software/",
    "116. Call Center > /call-center-software/",
    "117. Call Center Workforce Management > /call-center-workforce-management-software/",
    "118. Call Recording > /call-recording-software/",
    "119. Call Tracking > /call-tracking-software/",
    "120. Camp Management > /camp-management-software/",
    "121. Campaign Management > /campaign-management-software/",
    "122. Campground Management > /campground-management-software/",
    "123. Capacity Planning > /capacity-planning-software/",
    "124. Car Rental > /car-rental-software/",
    "125. Cardiology EMR > /cardiology-emr-software/",
    "126. Career Management > /career-management-software/",
    "127. Carpet Cleaning > /carpet-cleaning-software/",
    "128. Catalog Management > /catalog-management-software/",
    "129. Catering > /catering-software/",
    "130. Cemetery > /cemetery-software/",
    "131. Certification Tracking > /certification-tracking-software/",
    "132. Change Management > /change-management-software/",
    "133. Channel Management > /channel-management-software/",
    "134. Chargeback Management > /chargeback-management-software/",
    "135. Chatbot > /chatbot-software/",
    "136. Chemical > /chemical-software/",
    "137. Chemical Manufacturing > /chemical-manufacturing-software/",
    "138. Chiropractic > /chiropractic-software/",
    "139. Church Accounting > /church-accounting-software/",
    "140. Church Management > /church-management-software/",
    "141. Church Presentation > /church-presentation-software/",
    "142. Claims Processing > /claims-processing-software/",
    "143. Class Registration > /class-registration-software/",
    "144. Classroom Management > /classroom-management-software/",
    "145. Click Fraud > /click-fraud-software/",
    "146. Client Onboarding > /client-onboarding-software/",
    "147. Clinical Trial Management > /clinical-trial-management-software/",
    "148. Closed Captioning > /closed-captioning-software/",
    "149. Cloud Access Security Broker (CASB) > /cloud-access-security-broker-casb-software/",
    "150. Cloud Communication Platform > /cloud-communication-platform-software/",
    "151. Cloud Management > /cloud-management-software/",
    "152. Cloud PBX > /cloud-pbx-software/",
    "153. Cloud Security > /cloud-security-software/",
    "154. Cloud Storage > /cloud-storage-software/",
    "155. Club Management > /club-management-software/",
    "156. CMDB > /cmdb-software/",
    "157. CMMS > /cmms-software/",
    "158. Coaching > /coaching-software/",
    "159. Code Enforcement > /code-enforcement-software/",
    "160. Collaboration > /collaboration-software/",
    "161. Commercial Insurance > /commercial-insurance-software/",
    "162. Commercial Loan > /commercial-loan-software/",
    "163. Commercial Property Management > /commercial-property-management-software/",
    "164. Commercial Real Estate > /commercial-real-estate-software/",
    "165. Commission > /commission-software/",
    "166. Community > /community-software/",
    "167. Company Secretarial > /company-secretarial-software/",
    "168. Compensation Management > /compensation-management-software/",
    "169. Competitive Intelligence > /competitive-intelligence-software/",
    "170. Competitor Price Monitoring > /competitor-price-monitoring-software/",
    "171. Complaint Management > /complaint-management-software/",
    "172. Compliance > /compliance-software/",
    "173. Computer Repair Shop > /computer-repair-shop-software/",
    "174. Computer Security > /computer-security-software/",
    "175. Conference > /conference-software/",
    "176. Configuration Management Tools > /configuration-tools-software/",
    "177. Conflict Checking > /conflict-checking-software/",
    "178. Consignment > /consignment-software/",
    "179. Construction Accounting > /construction-accounting-software/",
    "180. Construction Bid Management > /construction-bid-management-software/",
    "181. Construction CRM > /construction-crm-software/",
    "182. Construction Estimating > /construction-estimating-software/",
    "183. Construction Management > /construction-management-software/",
    "184. Construction Scheduling > /construction-scheduling-software/",
    "185. Contact Center > /contact-center-software/",
    "186. Contact Center Quality Assurance > /contact-center-quality-assurance-software/",
    "187. Contact Management > /contact-management-software/",
    "188. Container Security > /container-security-software/",
    "189. Content Collaboration > /content-collaboration-software/",
    "190. Content Delivery Network > /content-delivery-network-software/",
    "191. Content Management > /content-management-software/",
    "192. Content Marketing > /content-marketing-software/",
    "193. Contest > /contest-software/",
    "194. Continuous Integration > /continuous-integration-software/",
    "195. Contract Management > /contract-management-software/",
    "196. Contractor Management > /contractor-management-software/",
    "197. Convenience Store > /convenience-store-software/",
    "198. Conversation Intelligence > /conversation-intelligence-software/",
    "199. Conversational AI Platform > /conversational-ai-platform-software/",
    "200. Conversational Marketing Platform > /conversational-marketing-platform-software/",
    "201. Corporate Social Responsibility (CSR) > /corporate-social-responsibility-software/",
    "202. Corporate Tax > /corporate-tax-software/",
    "203. Corporate Wellness > /corporate-wellness-software/",
    "204. Corrective and Preventive Action > /corrective-and-preventive-action-software/",
    "205. Courier > /courier-software/",
    "206. Course Authoring > /course-authoring-software/",
    "207. Court Management > /court-management-software/",
    "208. CPQ > /cpq-software/",
    "209. Creative Management > /creative-management-software/",
    "210. Credentialing > /credentialing-software/",
    "211. CRM > /customer-relationship-management-software/",
    "212. Cryptocurrency Exchange > /cryptocurrency-exchange-software/",
    "213. Cryptocurrency Wallets > /cryptocurrency-wallets-software/",
    "214. CTRM > /ctrm-software/",
    "215. Currency Exchange > /currency-exchange-software/",
    "216. Customer Advocacy > /customer-advocacy-software/",
    "217. Customer Communications Management > /customer-communications-management-software/",
    "218. Customer Data Platform > /customer-data-platform-software/",
    "219. Customer Engagement > /customer-engagement-software/",
    "220. Customer Experience > /customer-experience-software/",
    "221. Customer Identity and Access Management (CIAM) > /ciam-software/",
    "222. Customer Journey Mapping Tools > /customer-journey-mapping-tools-software/",
    "223. Customer Loyalty > /customer-loyalty-software/",
    "224. Customer Reference Management > /customer-reference-management-software/",
    "225. Customer Retention > /customer-retention-software/",
    "226. Customer Satisfaction > /customer-satisfaction-software/",
    "227. Customer Service > /customer-service-software/",
    "228. Customer Success > /customer-success-software/",
    "229. Customer Support > /customer-support-software/",
    "230. Customer Training > /customer-training-software/",
    "231. Cybersecurity > /cybersecurity-software/",
    "232. Dance Studio > /dance-studio-software/",
    "233. Dashboard > /dashboard-software/",
    "234. Data Analysis > /data-analysis-software/",
    "235. Data Catalog > /data-catalog-software/",
    "236. Data Center Management > /data-center-management-software/",
    "237. Data Collection > /data-collection-software/",
    "238. Data Discovery > /data-discovery-software/",
    "239. Data Entry > /data-entry-software/",
    "240. Data Extraction > /data-extraction-software/",
    "241. Data Governance > /data-governance-software/",
    "242. Data Loss Prevention > /data-loss-prevention-software/",
    "243. Data Management > /data-management-software/",
    "244. Data Management Platforms > /data-management-platforms-software/",
    "245. Data Mining > /data-mining-software/",
    "246. Data Preparation > /data-preparation-software/",
    "247. Data Privacy > /data-privacy-software/",
    "248. Data Quality > /data-quality-software/",
    "249. Data Visualization > /data-visualization-software/",
    "250. Data Warehouse > /data-warehouse-software/",
    "251. Database > /database-management-software/",
    "252. Database Monitoring > /database-monitoring-software/",
    "253. Daycare > /child-care-software/",
    "254. DDoS Protection > /ddos-protection-software/",
    "255. Debt Collection > /debt-collection-software/",
    "256. Decision Support > /decision-support-software/",
    "257. Deep Learning > /deep-learning-software/",
    "258. DEI (Diversity, Equity & Inclusion) > /dei-software/",
    "259. Delivery Management > /delivery-management-software/",
    "260. Demand Planning > /demand-planning-software/",
    "261. Demand Side Platform (DSP) > /demand-side-platform-software/",
    "262. Demo > /demo-software/",
    "263. Dental > /dental-software/",
    "264. Dental Charting > /dental-charting-software/",
    "265. Dental Imaging > /dental-imaging-software/",
    "266. Dermatology > /dermatology-software/",
    "267. Dermatology EMR > /dermatology-emr-software/",
    "268. Desk Booking > /desk-booking-software/",
    "269. Desktop as a Service (DaaS) > /daas-software/",
    "270. DevOps > /devops-software/",
    "271. Diagram > /diagram-software/",
    "272. Digital Adoption Platform > /digital-adoption-platform-software/",
    "273. Digital Asset Management > /digital-asset-management-software/",
    "274. Digital Experience Platforms (DXP) > /dxp-software/",
    "275. Digital Forensics > /digital-forensics-software/",
    "276. Digital Rights Management > /digital-rights-management-software/",
    "277. Digital Signage > /digital-signage-software/",
    "278. Digital Signature > /digital-signature-software/",
    "279. Digital Workplace > /digital-workplace-software/",
    "280. Direct Deposit Payroll > /direct-deposit-payroll-software/",
    "281. Direct Mail Automation > /direct-mail-automation-software/",
    "282. Directory > /directory-software/",
    "283. Disaster Recovery > /disaster-recovery-software/",
    "284. Disk Imaging > /disk-imaging-software/",
    "285. Display Advertising > /display-advertising-software/",
    "286. Distribution > /distribution-software/",
    "287. Distribution Accounting > /distribution-accounting-software/",
    "288. Dock Scheduling > /dock-scheduling-software/",
    "289. Docketing > /docketing-software/",
    "290. Document Control > /document-control-software/",
    "291. Document Generation > /document-generation-software/",
    "292. Document Management > /document-management-software/",
    "293. Document Version Control > /document-version-control-software/",
    "294. Donation Management > /donation-management-software/",
    "295. Driving School > /driving-school-software/",
    "296. Dropshipping > /dropshipping-software/",
    "297. Dry Cleaning > /dry-cleaning-software/",
    "298. e-Prescribing > /eprescribing-software/",
    "299. EAM > /eam-software/",
    "300. Earthwork Estimating > /earthwork-estimating-excavation-software/",
    "301. eCommerce > /ecommerce-software/",
    "302. EDI > /edi-software/",
    "303. EHS Management > /ehs-management-software/",
    "304. eLearning Authoring Tools > /elearning-authoring-tools-software/",
    "305. Electrical Contractor > /electrical-contractor-software/",
    "306. Electrical Design > /electrical-design-software/",
    "307. Electrical Estimating > /electrical-estimating-software/",
    "308. Electronic Data Capture > /electronic-data-capture-software/",
    "309. Electronic Discovery > /electronic-discovery-software/",
    "310. Electronic Lab Notebook > /electronic-lab-notebook-software/",
    "311. Electronic Medical Records > /electronic-medical-records-software/",
    "312. Email Archiving > /email-archiving-software/",
    "313. Email Management > /email-management-software/",
    "314. Email Marketing > /email-marketing-software/",
    "315. Email Security > /email-security-software/",
    "316. Email Signature > /email-signature-software/",
    "317. Email Tracking > /email-tracking-software/",
    "318. Email Verification Tools > /email-verification-tools-software/",
    "319. eMAR > /emar-software/",
    "320. Embedded Analytics > /embedded-analytics-software/",
    "321. Emergency Notification > /emergency-notification-software/",
    "322. Emissions Management > /emissions-management-software/",
    "323. Employee Advocacy > /employee-advocacy-software/",
    "324. Employee Communication Tools > /employee-communication-tools-software/",
    "325. Employee Engagement > /employee-engagement-software/",
    "326. Employee Monitoring > /employee-monitoring-software/",
    "327. Employee Recognition > /employee-recognition-software/",
    "328. Employee Scheduling > /employee-scheduling-software/",
    "329. EMS > /ems-software/",
    "330. Encryption > /encryption-software/",
    "331. Endpoint Detection and Response > /endpoint-detection-and-response-software/",
    "332. Endpoint Protection > /endpoint-protection-software/",
    "333. Energy Management > /energy-management-software/",
    "334. Engineering Accounting > /engineering-accounting-software/",
    "335. Engineering CAD > /engineering-cad-software/",
    "336. Enterprise Architecture > /enterprise-architecture-software/",
    "337. Enterprise Content Management > /enterprise-content-management-software/",
    "338. Enterprise Legal Management > /enterprise-legal-management-software/",
    "339. Enterprise Resource Planning > /enterprise-resource-planning-software/",
    "340. Enterprise Search > /enterprise-search-software/",
    "341. Enterprise Service Bus (ESB) > /esb-software/",
    "342. Entity Management > /entity-management-software/",
    "343. Environmental > /environmental-software/",
    "344. Equipment Maintenance > /equipment-maintenance-software/",
    "345. Equipment Rental > /equipment-rental-software/",
    "346. Equity Management > /equity-management-software/",
    "347. ERM > /erm-software/",
    "348. ESG > /esg-software/",
    "349. ETL > /etl-software/",
    "350. Event Booking > /event-booking-software/",
    "351. Event Check In > /event-check-in-software/",
    "352. Event Management > /event-management-software/",
    "353. Event Marketing > /event-marketing-software/",
    "354. Event Rental > /event-rental-software/",
    "355. Exam > /exam-software/",
    "356. Expense Report > /expense-report-software/",
    "357. Facility Management > /facility-management-software/",
    "358. Family Law > /family-law-software/",
    "359. Family Practice Electronic Medical Records > /family-practice-electronic-medical-records-emr-software/",
    "360. Farm Management > /farm-management-software/",
    "361. Fashion Design > /fashion-design-and-production-software/",
    "362. Fax Server > /fax-server-software/",
    "363. Festival Management > /festival-management-software/",
    "364. Field Sales > /field-sales-software/",
    "365. Field Service Management > /field-service-management-software/",
    "366. File Sharing > /file-sharing-software/",
    "367. File Sync > /file-sync-software/",
    "368. Financial Close > /financial-close-software/",
    "369. Financial CRM > /financial-crm-software/",
    "370. Financial Fraud Detection > /financial-fraud-detection-software/",
    "371. Financial Management > /financial-management-software/",
    "372. Financial Reporting > /financial-reporting-software/",
    "373. Financial Risk Management > /financial-risk-management-software/",
    "374. Financial Services > /financial-services-software/",
    "375. Fire Department > /fire-department-software/",
    "376. Firewall > /firewall-software/",
    "377. Fitness > /fitness-software/",
    "378. Fixed Asset Management > /fixed-asset-management-software/",
    "379. Fleet Maintenance > /fleet-maintenance-software/",
    "380. Fleet Management > /fleet-management-software/",
    "381. Floor Plan > /floor-plan-software/",
    "382. Florist > /florist-software/",
    "383. Flowchart > /flowchart-software/",
    "384. Food Costing > /food-costing-software/",
    "385. Food Delivery > /food-delivery-software/",
    "386. Food Manufacturing > /food-beverage-manufacturing-erp-software/",
    "387. Food Service Distribution > /food-service-distribution-software/",
    "388. Food Service Management > /food-service-management-software/",
    "389. Food Traceability > /food-traceability-software/",
    "390. Food Truck POS Systems > /food-truck-pos-systems-software/",
    "391. Forestry > /forestry-software/",
    "392. Form Builder > /form-builder-software/",
    "393. Forms Automation > /forms-automation-software/",
    "394. Franchise Management > /franchise-management-software/",
    "395. Freight > /freight-software/",
    "396. Fuel Management > /fuel-management-software/",
    "397. Fund Accounting > /fund-accounting-software/",
    "398. Fundraising > /fundraising-software/",
    "399. Funeral Home > /funeral-home-software/",
    "400. Game Development > /game-development-software/",
    "401. Gamification > /gamification-software/",
    "402. Gantt Chart > /gantt-chart-software/",
    "403. Garage Door > /garage-door-software/",
    "404. Garden Center > /garden-center-software/",
    "405. GDPR Compliance > /gdpr-compliance-software/",
    "406. General Ledger > /general-ledger-software/",
    "407. Generative AI > /generative-ai-software/",
    "408. GIS > /gis-software/",
    "409. Golf Course > /golf-course-software/",
    "410. Governance, Risk & Compliance (GRC) > /grc-software/",
    "411. Government > /government-software/",
    "412. GPS Tracking > /gps-tracking-software/",
    "413. Gradebook > /gradebook-software/",
    "414. Grant Management > /grant-management-software/",
    "415. Graphic Design > /graphic-design-software/",
    "416. Gym Management > /gym-management-software/",
    "417. Gymnastics > /gymnastics-software/",
    "418. Handyman > /handyman-software/",
    "419. Headless CMS > /headless-cms-platform-software/",
    "420. Headless eCommerce > /headless-ecommerce-platform-software/",
    "421. Healthcare CRM > /healthcare-crm-software/",
    "422. Healthcare LMS > /healthcare-lms-software/",
    "423. Heatmap > /heatmap-software/",
    "424. Hedge Fund > /hedge-fund-software/",
    "425. Help Desk > /help-desk-software/",
    "426. Higher Education > /higher-education-software/",
    "427. HIPAA Compliance > /hipaa-compliance-software/",
    "428. HOA > /hoa-software/",
    "429. Home Builder > /home-builder-software/",
    "430. Home Care > /home-care-software/",
    "431. Home Health Care > /home-health-care-software/",
    "432. Home Inspection > /home-inspection-software/",
    "433. Horse > /horse-software/",
    "434. Hospice > /hospice-software/",
    "435. Hospital Management > /hospital-management-software/",
    "436. Hospitality LMS > /hospitality-lms-software/",
    "437. Hospitality Property Management > /hospitality-property-management-software/",
    "438. Hostel Management > /hostel-management-software/",
    "439. Hotel Channel Management > /hotel-channel-management-software/",
    "440. HR Analytics > /hr-analytics-software/",
    "441. Human Resources > /human-resource-software/",
    "442. Human Services > /human-services-software/",
    "443. HVAC > /hvac-software/",
    "444. HVAC Estimating > /hvac-estimating-software/",
    "445. Hybrid Events > /hybrid-events-software/",
    "446. Idea Management > /idea-management-software/",
    "447. Identity Management > /identity-management-software/",
    "448. Identity Threat Detection and Response (ITDR) > /identity-threat-detection-and-response-software/",
    "449. Identity Verification > /identity-verification-software/",
    "450. Image Recognition > /image-recognition-software/",
    "451. Incident Management > /incident-management-software/",
    "452. Influencer Marketing > /influencer-marketing-software/",
    "453. Infrastructure as a Service (IaaS) > /infrastructure-as-a-service-solutions-software/",
    "454. Innovation Management > /innovation-software/",
    "455. Inside Sales > /inside-sales-software/",
    "456. Insight Engines > /insight-engines-software/",
    "457. Inspection > /inspection-software/",
    "458. Insurance > /insurance-agency-software/",
    "459. Insurance CRM > /insurance-crm-software/",
    "460. Insurance Policy > /insurance-policy-software/",
    "461. Insurance Rating > /insurance-rating-software/",
    "462. Integrated Development Environment (IDE) > /ide-software/",
    "463. Integrated Risk Management > /integrated-risk-management-software/",
    "464. Integration > /integration-software/",
    "465. Intellectual Property Management > /intellectual-property-management-software/",
    "466. Internal Communications > /internal-communications-software/",
    "467. Intranet > /intranet-software/",
    "468. Inventory Control > /inventory-control-software/",
    "469. Inventory Management > /inventory-management-software/",
    "470. Investigation Management > /investigation-management-software/",
    "471. Investment Management > /investment-management-software/",
    "472. IoT > /iot-software/",
    "473. IoT Analytics > /iot-analytics-software/",
    "474. iPaaS > /ipaas-software/",
    "475. iPad Kiosk > /ipad-kiosk-software/",
    "476. iPad POS > /ipad-pos-software/",
    "477. Issue Tracking > /issue-tracking-software/",
    "478. IT Asset Management > /it-asset-management-software/",
    "479. IT Documentation > /it-documentation-software/",
    "480. IT Management > /it-management-software/",
    "481. IT Project Management > /it-project-management-software/",
    "482. IT Service > /it-service-software/",
    "483. ITSM > /itsm-software/",
    "484. IVR > /ivr-software/",
    "485. IWMS > /iwms-software/",
    "486. Jail Management > /jail-management-software/",
    "487. Janitorial > /janitorial-software/",
    "488. Java CMS > /java-cms-software/",
    "489. Jewelry Store Management > /jewelry-store-management-software/",
    "490. Job Board > /job-board-software/",
    "491. Job Costing > /job-costing-software/",
    "492. Job Evaluation > /job-evaluation-software/",
    "493. Job Shop > /job-shop-software/",
    "494. K-12 > /k-12-software/",
    "495. Kanban Tools > /kanban-tools-software/",
    "496. Kennel > /kennel-software/",
    "497. Key Management > /key-management-software/",
    "498. Keyword Research Tools > /keyword-research-tools-software/",
    "499. Kiosk > /kiosk-software/",
    "500. Knowledge Base > /knowledge-base-software/",
    "501. Knowledge Management > /knowledge-management-software/",
    "502. KPI > /kpi-software/",
    "503. KYC > /kyc-software/",
    "504. Label Printing > /label-printing-software/",
    "505. Laboratory Information Management System > /laboratory-information-management-system-software/",
    "506. Laboratory Information Systems (LIS) > /laboratory-information-system-software/",
    "507. Land Management > /land-management-software/",
    "508. Landing Page > /landing-page-software/",
    "509. Landscape > /landscape-software/",
    "510. Language Learning > /language-learning-software/",
    "511. Law Enforcement > /law-enforcement-software/",
    "512. Law Practice Management > /law-practice-management-software/",
    "513. Lawn Care > /lawn-care-software/",
    "514. Lead Capture > /lead-capture-software/",
    "515. Lead Generation > /lead-generation-software/",
    "516. Lead Management > /lead-management-software/",
    "517. Lead Nurturing > /lead-nurturing-software/",
    "518. Learning Experience Platform > /learning-experience-platform-software/",
    "519. Learning Management System > /learning-management-system-software/",
    "520. Lease Accounting > /lease-accounting-software/",
    "521. Lease Management > /lease-management-software/",
    "522. Leave Management System > /leave-management-system-software/",
    "523. Legal Accounting > /legal-accounting-software/",
    "524. Legal Billing > /legal-billing-software/",
    "525. Legal Calendar > /legal-calendar-software/",
    "526. Legal Case Management > /legal-case-management-software/",
    "527. Legal Document Management > /legal-document-management-software/",
    "528. Legal Research > /legal-research-software/",
    "529. Library Automation > /library-automation-software/",
    "530. License Management > /license-management-software/",
    "531. Link Management Tools > /link-management-tools-software/",
    "532. Liquor Store POS > /liquor-store-pos-software/",
    "533. Live Chat > /live-chat-software/",
    "534. Live Streaming > /live-streaming-software/",
    "535. Load Balancing > /load-balancing-software/",
    "536. Load Testing > /load-testing-software/",
    "537. Loan Origination > /loan-origination-software/",
    "538. Loan Servicing > /loan-servicing-software/",
    "539. Local SEO Tools > /local-seo-tools-software/",
    "540. Localization > /localization-software/",
    "541. Location Intelligence > /location-intelligence-software/",
    "542. Locksmith > /locksmith-software/",
    "543. Log Analysis > /log-analysis-software/",
    "544. Log Management > /log-management-software/",
    "545. Logbook > /logbook-software/",
    "546. Logistics > /logistics-software/",
    "547. Long Term Care > /long-term-care-software/",
    "548. Lost and Found > /lost-and-found-software/",
    "549. Low Code Development Platform > /low-code-development-platform-software/",
    "550. Mac CRM > /mac-crm-software/",
    "551. Machine Learning > /machine-learning-software/",
    "552. Maid Service > /maid-service-software/",
    "553. Mailroom Management > /mailroom-management-software/",
    "554. Maintenance Management > /maintenance-management-software/",
    "555. Managed Service Providers (MSP) > /msp-software/",
    "556. Manufacturing > /manufacturing-software/",
    "557. Manufacturing Execution > /manufacturing-execution-software/",
    "558. Manufacturing Inventory Management > /manufacturing-inventory-management-software/",
    "559. Marine > /marine-software/",
    "560. Market Research > /market-research-software/",
    "561. Marketing Analytics > /marketing-analytics-software/",
    "562. Marketing Attribution > /marketing-attribution-software/",
    "563. Marketing Automation > /marketing-automation-software/",
    "564. Marketing Planning > /marketing-planning-software/",
    "565. Marketplace > /marketplace-software/",
    "566. Martial Arts > /martial-arts-software/",
    "567. Massage Therapy > /massage-therapy-software/",
    "568. Master Data Management > /master-data-management-software/",
    "569. Medical Accounting > /medical-accounting-software/",
    "570. Medical Billing > /medical-billing-software/",
    "571. Medical Imaging > /medical-imaging-software/",
    "572. Medical Inventory > /medical-inventory-software/",
    "573. Medical Lab > /medical-lab-software/",
    "574. Medical Practice Management > /medical-practice-management-software/",
    "575. Medical Scheduling > /medical-scheduling-software/",
    "576. Medical Spa > /medical-spa-software/",
    "577. Medical Transcription > /medical-transcription-software/",
    "578. Meeting > /meeting-software/",
    "579. Meeting Room Booking System > /meeting-room-booking-system-software/",
    "580. Membership Management > /membership-management-software/",
    "581. Mental Health > /mental-health-software/",
    "582. Mental Health EHR > /mental-health-ehr-software/",
    "583. Mentoring > /mentoring-software/",
    "584. Metadata Management > /metadata-management-software/",
    "585. Metal Fabrication > /metal-fabrication-software/",
    "586. Microlearning > /microlearning-software/",
    "587. Mileage Tracking > /mileage-tracking-software/",
    "588. Mind Mapping > /mind-mapping-software/",
    "589. Mining > /mining-software/",
    "590. MLM > /mlm-software/",
    "591. Mobile Analytics > /mobile-analytics-software/",
    "592. Mobile Banking > /mobile-banking-software/",
    "593. Mobile Content Management System > /mobile-content-management-system-software/",
    "594. Mobile Credit Card Processing > /mobile-credit-card-processing-software/",
    "595. Mobile Device Management > /mobile-device-management-software/",
    "596. Mobile Event Apps > /mobile-event-apps-software/",
    "597. Mobile Home Park Management > /mobile-home-park-management-software/",
    "598. Mobile Learning > /mobile-learning-software/",
    "599. Mobile Marketing > /mobile-marketing-software/",
    "600. Mobility > /mobility-software/",
    "601. Mortgage > /mortgage-and-loans-software/",
    "602. Motel > /motel-software/",
    "603. Moving > /moving-software/",
    "604. MRM > /mrm-software/",
    "605. MRP > /mrp-software/",
    "606. Multi-Channel eCommerce > /multi-channel-ecommerce-software/",
    "607. Multi-Country Payroll > /multicountry-payroll-software/",
    "608. Multi-Factor Authentication > /multi-factor-authentication-software/",
    "609. Municipal > /municipal-software/",
    "610. Museum > /museum-software/",
    "611. Music School > /music-school-software/",
    "612. Natural Language Processing (NLP) > /natural-language-processing-software/",
    "613. Network Access Control (NAC) > /network-access-control-software/",
    "614. Network Management > /network-management-software/",
    "615. Network Mapping > /network-mapping-software/",
    "616. Network Monitoring > /network-monitoring-software/",
    "617. Network Security > /network-security-software/",
    "618. Network Troubleshooting > /network-troubleshooting-software/",
    "619. Neurology EMR > /neurology-emr-software/",
    "620. NFT Creation > /nft-creation-software/",
    "621. No Code Platform > /no-code-platform-software/",
    "622. Nonprofit > /nonprofit-software/",
    "623. Nonprofit Accounting > /nonprofit-accounting-software/",
    "624. Nonprofit CRM > /nonprofit-crm-software/",
    "625. Nonprofit Project Management > /project-management-software-for-nonprofits-software/",
    "626. NoSQL Databases > /nosql-databases-software/",
    "627. Note-Taking > /note-taking-software/",
    "628. NPS > /nps-software/",
    "629. Nurse Scheduling > /nurse-scheduling-software/",
    "630. Nursing Home > /nursing-home-software/",
    "631. Nutrition Analysis > /nutrition-analysis-software/",
    "632. Nutritionist > /nutritionist-software/",
    "633. OBGYN EMR > /obgyn-emr-software/",
    "634. Observability > /observability-software/",
    "635. Occupational Health > /occupational-health-software/",
    "636. Occupational Therapy > /occupational-therapy-software/",
    "637. OCR > /ocr-software/",
    "638. OEE > /oee-software/",
    "639. Oil and Gas > /oil-and-gas-software/",
    "640. OKR > /okr-software/",
    "641. Onboarding > /onboarding-software/",
    "642. Online Banking > /online-banking-software/",
    "643. Online CRM > /online-crm-software/",
    "644. Online Ordering > /online-ordering-software/",
    "645. Online Proofing > /online-proofing-software/",
    "646. Operating Systems > /operating-systems-software/",
    "647. Ophthalmology EMR > /ophthalmology-emr-software/",
    "648. Optometry > /optometry-software/",
    "649. Order Entry > /order-entry-software/",
    "650. Order Fulfillment > /order-fulfillment-software/",
    "651. Order Management > /order-management-software/",
    "652. Org Chart > /org-chart-software/",
    "653. Orthopedic EMR > /orthopedic-emr-software/",
    "654. P&C Insurance > /p-c-insurance-software/",
    "655. Packaging > /packaging-software/",
    "656. PACS > /pacs-software/",
    "657. Pain Management EMR > /pain-management-emr-software/",
    "658. Parcel Audit > /parcel-audit-software/",
    "659. Parking Management > /parking-management-software/",
    "660. Parks and Recreation > /parks-and-recreation-software/",
    "661. Partner Management > /partner-management-software/",
    "662. Password Management > /password-management-software/",
    "663. Patch Management > /patch-management-software/",
    "664. Patient Case Management > /patient-case-management-software/",
    "665. Patient Engagement > /patient-engagement-software/",
    "666. Patient Management > /patient-management-software/",
    "667. Patient Portal > /patient-portal-software/",
    "668. Patient Scheduling > /patient-scheduling-software/",
    "669. Pawn Shop > /pawn-shop-software/",
    "670. Payment Processing > /payment-processing-software/",
    "671. Payroll > /payroll-software/",
    "672. PCI Compliance > /pci-compliance-software/",
    "673. PDF > /pdf-software/",
    "674. PDF Editor > /pdf-editor-software/",
    "675. Pediatric > /pediatric-software/",
    "676. PEO > /peo-software/",
    "677. Performance Management System > /performance-appraisal-software/",
    "678. Performance Testing > /performance-testing-software/",
    "679. Permit > /permit-software/",
    "680. Personal Trainer > /personal-trainer-software/",
    "681. Personalization > /personalization-software/",
    "682. Pest Control > /pest-control-software/",
    "683. Pet Grooming > /pet-grooming-software/",
    "684. Pet Sitting > /pet-sitting-software/",
    "685. Pharmacy > /pharmacy-software/",
    "686. Photo Editing > /photo-editing-software/",
    "687. Photography Studio > /photography-studio-software/",
    "688. Physical Security > /physical-security-software/",
    "689. Physical Therapy > /physical-therapy-software/",
    "690. Pilates Studio > /pilates-studio-software/",
    "691. PIM > /pim-software/",
    "692. Plagiarism Checker > /plagiarism-checker-software/",
    "693. Plastic Surgery > /plastic-surgery-software/",
    "694. Platform as a Service (PaaS) > /platform-as-a-service-software/",
    "695. Plumbing > /plumbing-software/",
    "696. Plumbing Estimating > /plumbing-estimating-software/",
    "697. Podcast Hosting > /podcast-hosting-software/",
    "698. Podiatry > /podiatry-software/",
    "699. Podiatry EMR > /podiatry-emr-software/",
    "700. Point of Sale > /point-of-sale-software/",
    "701. Policy Management > /policy-management-software/",
    "702. Political Campaign > /political-campaign-software/",
    "703. Polling > /polling-software/",
    "704. Pool Service > /pool-service-software/",
    "705. Portal > /portal-software/",
    "706. PPC > /ppc-software/",
    "707. Pre-employment Testing > /pre-employment-testing-software/",
    "708. Predictive Analytics > /predictive-analytics-software/",
    "709. Predictive Dialer > /predictive-dialer-software/",
    "710. Predictive Lead Scoring > /predictive-lead-scoring-software/",
    "711. Presentation > /presentation-software/",
    "712. Preventive Maintenance > /preventive-maintenance-software/",
    "713. Pricing Optimization > /pricing-optimization-software/",
    "714. Primary Care EHR > /primary-care-ehr-software/",
    "715. Print Estimating > /print-estimating-software/",
    "716. Print Management > /print-management-software/",
    "717. Privileged Access Management > /privileged-access-management-software/",
    "718. Proctoring > /proctoring-software/",
    "719. Procure to Pay > /procure-to-pay-software/",
    "720. Procurement > /procurement-software/",
    "721. Product Analytics > /product-analytics-software/",
    "722. Product Configurator > /product-configurator-software/",
    "723. Product Data Management > /product-data-management-software/",
    "724. Product Lifecycle Management > /product-lifecycle-management-software/",
    "725. Product Management > /product-management-software/",
    "726. Product Roadmap > /product-roadmap-software/",
    "727. Production Scheduling > /production-scheduling-software/",
    "728. Productivity > /productivity-software/",
    "729. Professional Services Automation > /professional-services-automation-software/",
    "730. Project Accounting > /project-accounting-software/",
    "731. Project Management > /project-management-software/",
    "732. Project Planning > /project-planning-software/",
    "733. Project Portfolio Management > /project-portfolio-management-software/",
    "734. Project Tracking > /project-tracking-software/",
    "735. Proofreading > /proofreading-software/",
    "736. Property Management > /rental-property-management-software/",
    "737. Property Management Accounting > /property-management-accounting-software/",
    "738. Proposal Management > /proposal-management-software/",
    "739. Prototyping > /prototyping-software/",
    "740. Psychiatry Electronic Medical Records > /psychiatry-electronic-medical-records-emr-software/",
    "741. Public Relations > /public-relations-software/",
    "742. Public Transportation > /public-transportation-software/",
    "743. Public Works > /public-works-software/",
    "744. Publishing and Subscriptions > /publishing-and-subscriptions-software/",
    "745. Punch List > /punch-list-software/",
    "746. Purchasing > /purchasing-software/",
    "747. Push Notifications > /push-notifications-software/",
    "748. Qualitative Data Analysis > /qualitative-data-analysis-software/",
    "749. Quality Management > /quality-management-software/",
    "750. Quoting > /quoting-software/",
    "751. Radiology > /radiology-software/",
    "752. RDBMS > /rdbms-software/",
    "753. Real Estate Accounting > /real-estate-accounting-software/",
    "754. Real Estate Agency > /real-estate-agency-software/",
    "755. Real Estate CMA > /real-estate-cma-software/",
    "756. Real Estate CRM > /real-estate-crm-software/",
    "757. Real Estate Property Management > /real-estate-property-management-software/",
    "758. Real Estate Transaction Management > /real-estate-transaction-management-software/",
    "759. Recruiting > /recruiting-software/",
    "760. Recruiting Agency > /recruiting-agency-software/",
    "761. Recruitment Marketing Platforms > /recruitment-marketing-platforms-software/",
    "762. Recurring Billing > /recurring-billing-software/",
    "763. Recycling > /recycling-software/",
    "764. Reference Check > /reference-check-software/",
    "765. Referral > /referral-software/",
    "766. Registration > /registration-software/",
    "767. Relocation > /relocation-software/",
    "768. Remodeling Estimating > /remodeling-estimating-software/",
    "769. Remote Desktop > /remote-desktop-software/",
    "770. Remote Monitoring and Management > /remote-monitoring-and-management-software/",
    "771. Remote Patient Monitoring > /remote-patient-monitoring-software/",
    "772. Remote Support > /remote-support-software/",
    "773. Remote Work > /remote-work-software/",
    "774. Rental > /rental-software/",
    "775. Reporting > /reporting-software/",
    "776. Reputation Management > /reputation-management-software/",
    "777. Requirements Management > /requirements-management-software/",
    "778. Reservations > /reservations-software/",
    "779. Residential Construction Estimating > /residential-construction-estimating-software/",
    "780. Resource Management > /resource-management-software/",
    "781. Restaurant Management > /restaurant-management-software/",
    "782. Restaurant POS > /restaurant-pos-software/",
    "783. Retail Execution > /retail-execution-software/",
    "784. Retail Management Systems > /retail-management-systems-software/",
    "785. Retail POS System > /retail-pos-system-software/",
    "786. Retargeting > /retargeting-software/",
    "787. Returns Management (RMS) > /returns-management-software/",
    "788. Revenue Cycle Management > /revenue-cycle-management-software/",
    "789. Revenue Management > /revenue-management-software/",
    "790. Revenue Recognition > /revenue-recognition-software/",
    "791. Review Management > /review-management-software/",
    "792. RFP > /rfp-software/",
    "793. Risk Management > /risk-management-software/",
    "794. Robotic Process Automation > /robotic-process-automation-software/",
    "795. Roofing > /roofing-software/",
    "796. Route Planning > /route-planning-software/",
    "797. SaaS Management > /saas-management-software/",
    "798. Safety Management > /safety-management-software/",
    "799. Sales Coaching > /sales-coaching-software/",
    "800. Sales Content Management > /sales-content-management-software/",
    "801. Sales Enablement > /sales-enablement-software/",
    "802. Sales Engagement Platform > /sales-engagement-platform-software/",
    "803. Sales Force Automation > /sales-force-automation-software/",
    "804. Sales Forecasting > /sales-forecasting-software/",
    "805. Sales Intelligence > /sales-intelligence-software/",
    "806. Sales Performance Management > /sales-performance-management-software/",
    "807. Sales Tax > /sales-tax-software/",
    "808. Sales Tracking > /sales-tracking-software/",
    "809. Salon > /salon-software/",
    "810. SCADA > /scada-software/",
    "811. Scheduling > /scheduling-software/",
    "812. Scholarship Management > /scholarship-management-software/",
    "813. School Accounting > /school-accounting-software/",
    "814. School Bus Routing > /school-bus-routing-software/",
    "815. School Facilities Management > /facilities-management-for-schools-software/",
    "816. School Management > /school-administration-software/",
    "817. Screen Recording > /screen-recording-software/",
    "818. Screen Sharing > /screen-sharing-software/",
    "819. Screenwriting > /screenwriting-software/",
    "820. Scrum > /scrum-software/",
    "821. Secure Email Gateway > /secure-email-gateway-software/",
    "822. Security Awareness Training > /security-awareness-training-software/",
    "823. Security System Installer > /security-system-installer-software/",
    "824. Self Storage > /self-storage-software/",
    "825. Self-Service Password Reset (SSPR) > /self-service-password-reset-software/",
    "826. SEO > /seo-software/",
    "827. Server Backup > /server-backup-software/",
    "828. Server Management > /server-management-software/",
    "829. Server Monitoring > /server-monitoring-software/",
    "830. Service Desk > /service-desk-software/",
    "831. Service Dispatch > /service-dispatch-software/",
    "832. Shipment Tracking > /shipment-tracking-software/",
    "833. Shipping > /shipping-software/",
    "834. Shopping Cart > /shopping-cart-software/",
    "835. SIEM > /siem-software/",
    "836. Simulation > /simulation-software/",
    "837. Single Sign On > /single-sign-on-software/",
    "838. Small Business CRM > /small-business-crm-software/",
    "839. Small Business eCommerce > /small-business-ecommerce-software/",
    "840. Small Business Loyalty Programs > /small-business-loyalty-programs-software/",
    "841. SMS Marketing > /sms-marketing-software/",
    "842. SMS Survey > /sms-survey-software/",
    "843. SOAR > /soar-software/",
    "844. Social CRM Tools > /social-crm-tools-software/",
    "845. Social Listening Tools > /social-listening-tools-software/",
    "846. Social Media Analytics Tools > /social-media-analytics-tools-software/",
    "847. Social Media Management > /social-media-management-software/",
    "848. Social Media Marketing > /social-media-marketing-software/",
    "849. Social Media Monitoring > /social-media-monitoring-software/",
    "850. Social Networking > /social-networking-software/",
    "851. Social Selling > /social-selling-software/",
    "852. Social Work Case Management > /social-work-case-management-software/",
    "853. Softphone > /softphone-software/",
    "854. Solar > /solar-software/",
    "855. Source Code Management > /source-code-management-software/",
    "856. Sourcing > /sourcing-software/",
    "857. Spa > /spa-software/",
    "858. Space Management > /space-management-software/",
    "859. SPC > /spc-software/",
    "860. Speech Analytics > /speech-analytics-software/",
    "861. Speech Recognition > /speech-recognition-software/",
    "862. Speech Therapy > /speech-therapy-software/",
    "863. Spend Management > /spend-management-software/",
    "864. Sports League > /sports-league-software/",
    "865. Spreadsheet > /spreadsheet-software/",
    "866. Staffing Agency > /staffing-agency-software/",
    "867. Static Application Security Testing (SAST) > /sast-software/",
    "868. Statistical Analysis > /statistical-analysis-software/",
    "869. Stock Portfolio Management > /stock-portfolio-management-software/",
    "870. Store Locator > /store-locator-software/",
    "871. Strategic Planning > /strategic-planning-software/",
    "872. Student Engagement Platform > /student-engagement-platform-software/",
    "873. Student Information System > /student-information-system-software/",
    "874. Subcontractor > /subcontractor-software/",
    "875. Subscription Management > /subscription-management-software/",
    "876. Substance Abuse EMR > /substance-abuse-emr-software/",
    "877. Succession Planning > /succession-planning-software/",
    "878. Supply Chain Management > /supply-chain-management-software/",
    "879. Survey > /survey-software/",
    "880. Sustainability > /sustainability-software/",
    "881. Swim School > /swim-school-software/",
    "882. Takeoff > /takeoff-software/",
    "883. Talent Management > /talent-management-software/",
    "884. Task Management > /task-management-software/",
    "885. Tattoo Studio > /tattoo-studio-software/",
    "886. Tax Practice Management > /tax-practice-management-software/",
    "887. Tax Preparation > /tax-preparation-software/",
    "888. Team Communication > /team-communication-software/",
    "889. Team Management > /team-management-software/",
    "890. Telecom Expense Management > /telecom-expense-management-software/",
    "891. Telemarketing > /telemarketing-software/",
    "892. Telemedicine > /telemedicine-software/",
    "893. Telephony > /telephony-software/",
    "894. Test Management Tools > /test-management-tools-software/",
    "895. Text Mining > /text-mining-software/",
    "896. Text to Image > /text-to-image-software/",
    "897. Text-To-Speech > /text-to-speech-software/",
    "898. Therapy > /therapy-software/",
    "899. Therapy Notes > /therapy-notes-software/",
    "900. Third Party Logistics (3PL) > /3pl-software/",
    "901. Threat Intelligence > /threat-intelligence-software/",
    "902. Ticketing > /ticketing-software/",
    "903. Time and Expense > /time-and-expense-software/",
    "904. Time Clock > /time-clock-software/",
    "905. Time Tracking > /time-tracking-software/",
    "906. Timeshare > /timeshare-software/",
    "907. Tool Management > /tool-management-software/",
    "908. Tour Operator > /tour-operator-software/",
    "909. Towing > /towing-software/",
    "910. Trade Promotion Management > /trade-promotion-management-software/",
    "911. Training > /training-software/",
    "912. Transactional Email > /transactional-email-software/",
    "913. Transcription > /transcription-software/",
    "914. Translation Management > /translation-management-software/",
    "915. Transportation Dispatch > /transportation-dispatch-software/",
    "916. Transportation Management > /transportation-management-software/",
    "917. Travel Agency > /travel-agency-software/",
    "918. Travel Management > /travel-management-software/",
    "919. Treasury > /treasury-software/",
    "920. Trucking > /trucking-software/",
    "921. Trucking Accounting > /trucking-accounting-software/",
    "922. Trust Accounting > /trust-accounting-software/",
    "923. Tutoring > /tutoring-software/",
    "924. Unified Communications > /unified-communications-software/",
    "925. Unified Endpoint Management (UEM) > /unified-endpoint-management-software/",
    "926. Urgent Care EMR > /urgent-care-emr-software/",
    "927. URL Shortener > /url-shortener-software/",
    "928. Urology EMR > /urology-emr-software/",
    "929. User Experience (UX) > /ux-software/",
    "930. User Testing > /user-testing-software/",
    "931. Utility Billing > /utility-billing-software/",
    "932. Utility Management Systems > /utility-management-systems-software/",
    "933. Vacation Rental > /vacation-rental-software/",
    "934. Vaccine Management > /vaccine-management-software/",
    "935. VDI > /vdi-software/",
    "936. Vector Graphics > /vector-graphics-software/",
    "937. Vendor Management > /vendor-management-software/",
    "938. Venue Management > /venue-management-software/",
    "939. Veterinary > /veterinary-software/",
    "940. Video Conferencing > /video-conferencing-software/",
    "941. Video Editing > /video-editing-software/",
    "942. Video Hosting > /video-hosting-software/",
    "943. Video Interviewing > /video-interviewing-software/",
    "944. Video Making > /video-making-software/",
    "945. Video Management > /video-management-software/",
    "946. Video Marketing > /video-marketing-software/",
    "947. Video Surveillance > /video-surveillance-software/",
    "948. Virtual Assistant > /virtual-assistant-software/",
    "949. Virtual Classroom > /virtual-classroom-software/",
    "950. Virtual Data Room > /virtual-data-room-software/",
    "951. Virtual Event > /virtual-event-software/",
    "952. Virtual Machine > /virtual-machine-software/",
    "953. Virtual Private Server > /virtual-private-server-software/",
    "954. Virtual Reality (VR) > /vr-software/",
    "955. Virtual Tour > /virtual-tour-software/",
    "956. Virtualization > /virtualization-software/",
    "957. Visitor Management > /visitor-management-software/",
    "958. Visual Search > /visual-search-software/",
    "959. VoIP > /voip-software/",
    "960. Volunteer Management > /volunteer-management-software/",
    "961. Voting > /voting-software/",
    "962. VPN > /vpn-software/",
    "963. Vulnerability Management > /vulnerability-management-software/",
    "964. Vulnerability Scanner > /vulnerability-scanner-software/",
    "965. Waitlist > /waitlist-software/",
    "966. Waiver > /waiver-software/",
    "967. Warehouse Management > /warehouse-management-software/",
    "968. Warranty Management > /warranty-management-software/",
    "969. Waste Management > /waste-management-software/",
    "970. Web Analytics > /web-analytics-software/",
    "971. Web Conferencing > /web-conferencing-software/",
    "972. Web Content Management > /web-content-management-software/",
    "973. Web Scraping > /web-scraping-software/",
    "974. Web to Print > /web-to-print-software/",
    "975. Webinar > /webinar-software/",
    "976. Website Accessibility > /website-accessibility-software/",
    "977. Website Builder > /website-builder-software/",
    "978. Website Monitoring > /website-monitoring-software/",
    "979. Website Optimization Tools > /website-optimization-tools-software/",
    "980. Website Security > /website-security-software/",
    "981. Whistleblowing > /whistleblowing-software/",
    "982. Whiteboard > /whiteboard-software/",
    "983. Winery > /winery-software/",
    "984. Wireframe > /wireframe-software/",
    "985. Wireless Expense Management > /wireless-expense-management-software/",
    "986. Work Order > /work-order-software/",
    "987. Workflow Management > /workflow-management-software/",
    "988. Workforce Management > /workforce-management-software/",
    "989. Worship > /worship-software/",
    "990. XDR (Extended Detection & Response) > /xdr-software/",
    "991. Yard Management > /yard-management-software/",
    "992. Yoga Studio > /yoga-studio-software/",
    "993. Zoo > /zoo-software/",
]
TOTAL_CATEGORY_COUNT = len(CATEGORY_LIST)


def mark_as_done(dir_path: str):
    try:
        with open(os.path.join(dir_path, DONE_MARKER_NAME), "w") as f:
            f.write("done")
    except:
        traceback.print_exc()


def is_done(dir_path: str) -> bool:
    ret = False
    try:
        ret = os.path.isfile(os.path.join(dir_path, DONE_MARKER_NAME))
    except:
        traceback.print_exc()
    return ret


def get_cookie(url: str, wait_elem_selector: str) -> Optional[str]:
    cookie_header = None
    if CHROME != None:
        CHROME.run_script("localStorage.clear(); sessionStorage.clear();")
        CHROME.clear_cookie()
        while not CHROME.goto(
            url2go=url,
            wait_elem_selector=wait_elem_selector,
            wait_timeout=30.0,
        ):
            pass

        while True:
            cookies = CHROME.cookie(COOKIE_DOMAIN)
            if cookies != None:
                cookie_header = ""
                for cookie in cookies:
                    cookie_header += f"{cookie['name']}={cookie['value']}; "
                cookie_header = cookie_header.strip().rstrip(";")

                if cookie_header == "":
                    # log_err("Cookie is empty, Retry get cookie")
                    time.sleep(1)
                else:
                    break
            else:
                log_err("Cookie is none")
    else:
        log_err("chrome is none")
    return cookie_header


def fetch(url: str, delay: float = 0.0) -> Optional[BeautifulSoup]:
    global COOKIE

    ret = None
    try:
        if not url.startswith(BASE_URL):
            url = BASE_URL + url

        while True:
            try:
                time.sleep(delay)

                resp = requests.get(
                    url,
                    headers={
                        "Cookie": COOKIE,
                        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                        "Sec-Ch-Ua-Mobile": "?0",
                        "Sec-Ch-Ua-Platform": '"Windows"',
                        "Upgrade-Insecure-Requests": "1",
                        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
                        "User-Agent": USER_AGENT,
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                        # "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Priority": "u=0, i",
                        "Connection": "close",
                    },
                    verify=False,
                    timeout=30.0,
                )

                if resp.status_code == 200:
                    ret = BeautifulSoup(resp.text, "html.parser")
                    break
                else:
                    log_err(f"request error: {resp.status_code}")

                log_inf("fetch new cookie")
                COOKIE = get_cookie(
                    url=url,
                    wait_elem_selector="span.dropdown-trigger.text-primary-base.inline-flex.cursor-pointer.items-baseline.font-semibold",
                )
                log_inf(f"cookie > {COOKIE}")
            except:
                traceback.print_exc()
    except:
        traceback.print_exc()
    return ret


def fetch_reviews2(url: str, delay: float = 0.0) -> any:
    global COOKIE

    ret = None
    try:
        if not url.startswith(BASE_URL):
            url = BASE_URL + url

        while True:
            try:
                time.sleep(delay)
                resp = requests.post(
                    url,
                    headers={
                        "Cookie": COOKIE,
                        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                        "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(spotlight)%22%2C%7B%22children%22%3A%5B%22p%22%2C%7B%22children%22%3A%5B%5B%22seoId%22%2C%2210019949%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22VideoExpress%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22reviews%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                        "Sec-Ch-Ua-Mobile": "?0",
                        "User-Agent": USER_AGENT,
                        "Content-Type": "text/plain;charset=UTF-8",
                        "Accept": "text/x-component",
                        # "Accept-Encoding": "gzip, deflate",
                        "Next-Action": "3a2d6332108300b9ae3be8707d1bcfe7db2c465f",
                        "Sec-Ch-Ua-Platform": '"Windows"',
                        "Origin": "https://www.capterra.com",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://www.capterra.com/p/10019949/VideoExpress/reviews/",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Priority": "u=1, i",
                    },
                    data='[{"sort":"MOST_HELPFUL","after":"YXJyYXljb25uZWN0aW9uOjI0"}]',
                    verify=False,
                    timeout=15.0,
                )

                if resp.status_code == 200:
                    reviews_str = (
                        '{"textReviews":'
                        + resp.text.strip().replace("\r", "").split("\n")[-1].split('1:{"textReviews":', 1)[1]
                    )
                    ret = json.loads(reviews_str)
                    break
                else:
                    log_err(f"request error: {resp.status_code}")

                log_inf("fetch new cookie")
                COOKIE = get_cookie(
                    url=url,
                    wait_elem_selector="span.dropdown-trigger.text-primary-base.inline-flex.cursor-pointer.items-baseline.font-semibold",
                )
                log_inf(f"cookie > {COOKIE}")
            except:
                traceback.print_exc()
    except:
        traceback.print_exc()
    return ret


def crawl_category(category_index: int):
    try:
        category_str = CATEGORY_LIST[category_index]
        category_name = category_str.split(">", 1)[0].split(".", 1)[1].strip()
        category_link = category_str.split(">", 1)[1].strip()

        category_dir = os.path.join(OUTPUT_DIR, f"{category_index}.{category_name}")
        os.makedirs(category_dir, exist_ok=True)

        if is_done(category_dir):
            log_inf(f"category `{category_index}. {category_name}` is already done")
        else:
            log_inf(f"category `{category_index}. {category_name}` > {category_link}")

            # fetch company list
            soup = fetch(category_link)
            if soup != None:
                product_count_elem = soup.select_one("div.leading-xl.mb-md.font-sans.text-xl.font-bold")
                if product_count_elem != None:
                    product_count = product_count_elem.text.split("(", 1)[1].split(")")[0].strip()
                    product_count = int(product_count)

                    # loop pages
                    page_count = int((product_count + PAGE_SIZE - 1) / PAGE_SIZE)
                    for page_index in range(page_count):
                        page_dir = os.path.join(category_dir, f"{page_index}")
                        os.makedirs(page_dir, exist_ok=True)

                        if is_done(page_dir):
                            log_inf(f"page {page_index} is already done")
                            continue

                        if page_index > 0:
                            page_link = category_link + f"?page={page_index+1}"
                            log_inf(f"page {page_index} / {page_count} > {page_link}")
                            soup = fetch(page_link)
                        else:
                            log_inf(f"page 0 / {page_count}")

                        if soup == None:
                            log_err(f"failed fetch page {page_index}")
                            continue

                        # loop products
                        product_desc_elems = soup.select("div.text-neutral-99.text-md.pb-lg")
                        product_link_elems = soup.select("div.pr-xl.justify-start>a")
                        for i, product_link_elem in enumerate(product_link_elems):
                            product_path = os.path.join(page_dir, f"{i}.json")
                            if os.path.isfile(product_path):
                                log_inf(f"product {i} is already done")
                                continue

                            product_link = product_link_elem.attrs["href"]
                            log_inf(f"product {i} > {product_link}")
                            soup = fetch(product_link)
                            if soup is None:
                                log_err("failed fetch product page")
                                continue

                            # scrap product
                            tmp_path = product_path + ".tmp"
                            product = {}

                            # product name
                            name_elem = soup.select_one("h1")
                            if name_elem != None:
                                product["name"] = name_elem.text.strip()
                            else:
                                log_err("name elem is none")
                                product["name"] = None

                            # description
                            product["desc"] = product_desc_elems[i].text.strip()

                            # rating score & review count
                            rating_elem = soup.select_one("span.sb.type-40.star-rating-label")
                            if rating_elem != None:
                                rating_str = rating_elem.text.strip()
                                product["rating_score"] = float(rating_str.split("(", 1)[0].strip())
                                product["review_count"] = int(rating_str.split("(", 1)[1].split(")")[0].strip())
                            else:
                                product["rating_score"] = None
                                product["review_count"] = None

                            # url
                            product["url"] = product_link

                            # recommendation percentage
                            product_recommend_elem = soup.select_one(
                                "div[data-testid=likelihood-section]>div:nth-child(2)>div>progress"
                            )
                            if product_recommend_elem != None:
                                product["recommend"] = float(product_recommend_elem.attrs["value"])
                            else:
                                log_err("product recommend elem is none")
                                product["recommend"] = None

                            product["reviews"] = []
                            if product["review_count"] in [None, 0]:
                                # reviews 0 ~ 24
                                review_link = product_link + "reviews/"
                                soup = fetch(review_link)
                                if soup != None:
                                    review_elems = soup.select("div[data-test-id='review-card']")
                                    for review_elem in review_elems:
                                        review = {}

                                        # user
                                        user_elem = review_elem.select_one("div.mb-3xs")
                                        if user_elem != None:
                                            review["user"] = user_elem.text.strip()
                                        else:
                                            log_err("review elem is none")
                                            review["user"] = None

                                        # title
                                        title_elem = review_elem.select_one("div.mt-2xl")
                                        if title_elem != None:
                                            review["title"] = title_elem.text.strip('"').strip()
                                        else:
                                            log_err("title elem is none")
                                            review["title"] = None

                                        # overall
                                        overall_elem = review_elem.select_one("div[data-testid=overall-content]")
                                        if overall_elem != None:
                                            review["overall"] = overall_elem.text.replace("Overall:", "").strip()
                                        else:
                                            log_err("overall elem is none")
                                            review["overall"] = None

                                        # pros
                                        pros_elem = review_elem.select_one("div[data-testid=pros-content]")
                                        if pros_elem != None:
                                            review["pros"] = pros_elem.text.replace("Pros:", "").strip()
                                        else:
                                            log_err("pros elem is none")
                                            review["pros"] = None

                                        # cons
                                        cons_elem = review_elem.select_one("div[data-testid=cons-content]")
                                        if cons_elem != None:
                                            review["cons"] = cons_elem.text.replace("Cons:", "").strip()
                                        else:
                                            log_err("cons elem is none")
                                            review["cons"] = None

                                        # rating
                                        rating_elem = review_elem.select_one("span.star-rating-label>span")
                                        if rating_elem != None:
                                            review["rating"] = float(rating_elem.text.strip())
                                        else:
                                            log_err("rating elem is none")
                                            review["rating"] = None

                                        # recommend
                                        recommend_elem = review_elem.select_one("progress")
                                        if recommend_elem != None:
                                            review["recommend"] = float(recommend_elem.attrs["value"].strip())
                                        else:
                                            log_err("recommend elem is none")
                                            review["recommend"] = None

                                        product["reviews"].append(review)
                                else:
                                    log_err("failed fetch review page")

                                # reviews 25 ~ 50
                                resp_reviews = fetch_reviews2(review_link)["textReviews"]
                                for resp_review in resp_reviews:
                                    review = {}

                                    # user
                                    review["user"] = resp_review["reviewer"]["fullName"]

                                    # title
                                    review["title"] = resp_review["title"]

                                    # overall
                                    review["overall"] = resp_review["generalComments"]

                                    # pros
                                    review["pros"] = resp_review["prosText"]

                                    # cons
                                    review["cons"] = resp_review["consText"]

                                    # rating
                                    review["rating"] = float(resp_review["overallRating"])

                                    # recommend
                                    review["recommend"] = float(resp_review["recommendationRating"])

                                    product["reviews"].append(review)

                            # category link
                            product["category_url"] = category_link

                            with open(tmp_path, "w") as file:
                                json.dump(product, file, indent=2)
                            os.rename(tmp_path, product_path)
                        mark_as_done(page_dir)
                else:
                    log_err("product count elem is none.")
            else:
                log_err("failed fetch page content")
        mark_as_done(category_dir)
    except:
        traceback.print_exc()


def work(start: int, count: int):
    try:
        global CHROME, USER_AGENT

        begin_index = start
        end_index = min(TOTAL_CATEGORY_COUNT, start + count)
        if count == 0:
            end_index = TOTAL_CATEGORY_COUNT

        log_inf(f"Categories: From {begin_index} To {end_index}")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Categories: From {begin_index} To {end_index}")

        CHROME = Chrome(
            width=800 + randint(0, 200),
            height=600 + randint(0, 100),
            # user_data_dir=os.path.join(TEMP_DIR, f"profile_{start}_{count}_{datetime.now().timestamp()}"),
            block_image=True,
            user_data_dir=os.path.join(TEMP_DIR, f"profile_{start}_{count}"),
        )
        CHROME.start()
        USER_AGENT = CHROME.run_script("navigator.userAgent")

        for i in range(begin_index, end_index):
            crawl_category(category_index=i)

        CHROME.quit()
        log_inf("All done.")
    except:
        traceback.print_exc()


def main():
    global STATE, FROM_CITY, CITY_COUNT
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        dest="start",
        type=int,
        default=0,
        required=False,
        help="Start category index. Default is 0.",
    )
    parser.add_argument(
        "--count",
        dest="count",
        type=int,
        default=0,
        required=False,
        help="Category count. Default is 0 which means all the following categories.",
    )
    args = parser.parse_args()

    work(start=args.start, count=args.count)
    input("Press ENTER to exit.")


if __name__ == "__main__":
    main()
