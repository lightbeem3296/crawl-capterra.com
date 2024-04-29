# Category List

## URL

<https://www.capterra.com/>

## JavaScript

```javascript
box = document.querySelectorAll("div.nb-m-auto.nb-max-w-limiter")[2];
parents = box.querySelectorAll("div.nb-accordion-section-container");
var k = 0;
for (var i in parents) {
    try {
        parent = parents[i];
        parentName = parent.querySelector("h3").textContent;
        childs = parent.querySelectorAll("li>a");
        for (var j in childs) {
            try {
                child = childs[j];
                childName = child.textContent;
                childLink = child.getAttribute("href");
                console.log(`${k}. ${i}.${j} > ${parentName} > ${childName} > ${childLink}`);
                k++;
            } catch (e) {}
        }
    } catch (e) {}
}
```

## Catagories

0. 0.0 > Accounting & Finance > Accounting > /accounting-software/
1. 0.1 > Accounting & Finance > Accounting Practice Management > /accounting-practice-management-software/
2. 0.2 > Accounting & Finance > Accounts Payable > /accounts-payable-software/
3. 0.3 > Accounting & Finance > Accounts Receivable > /accounts-receivable-software/
4. 0.4 > Accounting & Finance > Asset Tracking > /asset-tracking-software/
5. 0.5 > Accounting & Finance > Auto Dealer Accounting > /auto-dealer-accounting-software/
6. 0.6 > Accounting & Finance > Billing and Invoicing > /billing-and-invoicing-software/
7. 0.7 > Accounting & Finance > Bookkeeper > /bookkeeper-software/
8. 0.8 > Accounting & Finance > Budgeting > /budgeting-software/
9. 0.9 > Accounting & Finance > Corporate Tax > /corporate-tax-software/
10. 0.10 > Accounting & Finance > EAM > /eam-software/
11. 0.11 > Accounting & Finance > Equity Management > /equity-management-software/
12. 0.12 > Accounting & Finance > Expense Report > /expense-report-software/
13. 0.13 > Accounting & Finance > Financial Management > /financial-management-software/
14. 0.14 > Accounting & Finance > Financial Services > /financial-services-software/
15. 0.15 > Accounting & Finance > Fixed Asset Management > /fixed-asset-management-software/
16. 0.16 > Accounting & Finance > Lease Accounting > /lease-accounting-software/
17. 0.17 > Accounting & Finance > Mobile Credit Card Processing > /mobile-credit-card-processing-software/
18. 0.18 > Accounting & Finance > Nonprofit Accounting > /nonprofit-accounting-software/
19. 0.19 > Accounting & Finance > Online Banking > /online-banking-software/
20. 0.20 > Accounting & Finance > Purchasing > /purchasing-software/
21. 0.21 > Accounting & Finance > Recurring Billing > /recurring-billing-software/
22. 0.22 > Accounting & Finance > Revenue Management > /revenue-management-software/
23. 0.23 > Accounting & Finance > Sourcing > /sourcing-software/
24. 0.24 > Accounting & Finance > Spend management > /spend-management-software/
25. 0.25 > Accounting & Finance > Tax Practice Management > /tax-practice-management-software/
26. 0.26 > Accounting & Finance > Treasury > /treasury-software/
27. 1.0 > Agriculture & Animal > Animal Shelter > /animal-shelter-software/
28. 1.1 > Agriculture & Animal > Farm Management > /farm-management-software/
29. 1.2 > Agriculture & Animal > Horse > /horse-software/
30. 1.3 > Agriculture & Animal > Pet Grooming > /pet-grooming-software/
31. 1.4 > Agriculture & Animal > Pet Sitting > /pet-sitting-software/
32. 1.5 > Agriculture & Animal > Veterinary > /veterinary-software/
33. 1.6 > Agriculture & Animal > Zoo > /zoo-software/
34. 2.0 > Banking & Loans > AML > /aml-software/
35. 2.1 > Banking & Loans > Banking Systems > /banking-systems-software/
36. 2.2 > Banking & Loans > Commercial Loan > /commercial-loan-software/
37. 2.3 > Banking & Loans > Currency Exchange > /currency-exchange-software/
38. 2.4 > Banking & Loans > Debt Collection > /debt-collection-software/
39. 2.5 > Banking & Loans > Financial CRM > /financial-crm-software/
40. 2.6 > Banking & Loans > Financial Fraud Detection > /financial-fraud-detection-software/
41. 2.7 > Banking & Loans > Financial Risk Management > /financial-risk-management-software/
42. 2.8 > Banking & Loans > Hedge Fund > /hedge-fund-software/
43. 2.9 > Banking & Loans > Investment Management > /investment-management-software/
44. 2.10 > Banking & Loans > Loan Origination > /loan-origination-software/
45. 2.11 > Banking & Loans > Loan Servicing > /loan-servicing-software/
46. 2.12 > Banking & Loans > Mobile Banking > /mobile-banking-software/
47. 2.13 > Banking & Loans > Mortgage and Loans > /mortgage-and-loans-software/
48. 2.14 > Banking & Loans > Stock Portfolio Management > /stock-portfolio-management-software/
49. 3.0 > Business Operations > Bankruptcy > /bankruptcy-software/
50. 3.1 > Business Operations > Board Management > /board-management-software/
51. 3.2 > Business Operations > Business Intelligence > /business-intelligence-software/
52. 3.3 > Business Operations > Business Management > /business-management-software/
53. 3.4 > Business Operations > Business Performance Management > /business-performance-management-software/
54. 3.5 > Business Operations > Business Plan > /business-plan-software/
55. 3.6 > Business Operations > Business Process Management > /business-process-management-software/
56. 3.7 > Business Operations > Company Secretarial > /company-secretarial-software/
57. 3.8 > Business Operations > Competitive Intelligence > /competitive-intelligence-software/
58. 3.9 > Business Operations > Contract Management > /contract-management-software/
59. 3.10 > Business Operations > Dashboard > /dashboard-software/
60. 3.11 > Business Operations > Decision Support > /decision-support-software/
61. 3.12 > Business Operations > Enterprise Resource Planning > /enterprise-resource-planning-software/
62. 3.13 > Business Operations > Financial Reporting > /financial-reporting-software/
63. 3.14 > Business Operations > Flowchart > /flowchart-software/
64. 3.15 > Business Operations > Location Intelligence > /location-intelligence-software/
65. 3.16 > Business Operations > OKR > /okr-software/
66. 3.17 > Business Operations > Policy Management > /policy-management-software/
67. 3.18 > Business Operations > Procurement > /procurement-software/
68. 3.19 > Business Operations > Productivity > /productivity-software/
69. 3.20 > Business Operations > Remote Work > /remote-work-software/
70. 3.21 > Business Operations > Reporting > /reporting-software/
71. 3.22 > Business Operations > RFP > /rfp-software/
72. 3.23 > Business Operations > Statistical Analysis > /statistical-analysis-software/
73. 3.24 > Business Operations > Strategic Planning > /strategic-planning-software/
74. 4.0 > Communications & Media > Auto Dialer > /auto-dialer-software/
75. 4.1 > Communications & Media > Billing and Provisioning > /billing-and-provisioning-software/
76. 4.2 > Communications & Media > Business Phone Systems > /business-phone-systems-software/
77. 4.3 > Communications & Media > Call Accounting > /call-accounting-software/
78. 4.4 > Communications & Media > Call Recording > /call-recording-software/
79. 4.5 > Communications & Media > Call Tracking > /call-tracking-software/
80. 4.6 > Communications & Media > Cloud Communication Platform > /cloud-communication-platform-software/
81. 4.7 > Communications & Media > Cloud PBX > /cloud-pbx-software/
82. 4.8 > Communications & Media > Collaboration > /collaboration-software/
83. 4.9 > Communications & Media > Community > /community-software/
84. 4.10 > Communications & Media > Digital Workplace > /digital-workplace-software/
85. 4.11 > Communications & Media > Fax Server > /fax-server-software/
86. 4.12 > Communications & Media > Internal Communications > /internal-communications-software/
87. 4.13 > Communications & Media > IVR > /ivr-software/
88. 4.14 > Communications & Media > Mobile Device Management > /mobile-device-management-software/
89. 4.15 > Communications & Media > Predictive Dialer > /predictive-dialer-software/
90. 4.16 > Communications & Media > Presentation > /presentation-software/
91. 4.17 > Communications & Media > Print Estimating > /print-estimating-software/
92. 4.18 > Communications & Media > Publishing and Subscriptions > /publishing-and-subscriptions-software/
93. 4.19 > Communications & Media > Screen Recording > /screen-recording-software/
94. 4.20 > Communications & Media > Screen Sharing > /screen-sharing-software/
95. 4.21 > Communications & Media > Softphone  > /softphone-software/
96. 4.22 > Communications & Media > Speech Recognition > /speech-recognition-software/
97. 4.23 > Communications & Media > Subscription Management > /subscription-management-software/
98. 4.24 > Communications & Media > Team Communication > /team-communication-software/
99. 4.25 > Communications & Media > Telecom Expense Management > /telecom-expense-management-software/
100. 4.26 > Communications & Media > Telephony > /telephony-software/
101. 4.27 > Communications & Media > Transcription > /transcription-software/
102. 4.28 > Communications & Media > Translation Management > /translation-management-software/
103. 4.29 > Communications & Media > Unified Communications > /unified-communications-software/
104. 4.30 > Communications & Media > Video Conferencing  > /video-conferencing-software/
105. 4.31 > Communications & Media > Video Editing > /video-editing-software/
106. 4.32 > Communications & Media > Video Making > /video-making-software/
107. 4.33 > Communications & Media > Video Management > /video-management-software/
108. 4.34 > Communications & Media > VoIP > /voip-software/
109. 4.35 > Communications & Media > Web Conferencing > /web-conferencing-software/
110. 4.36 > Communications & Media > Webinar > /webinar-software/
111. 4.37 > Communications & Media > Wireless Expense Management > /wireless-expense-management-software/
112. 5.0 > Compliance & Risk Management > Accreditation Management > /accreditation-management-software/
113. 5.1 > Compliance & Risk Management > Audit > /audit-software/
114. 5.2 > Compliance & Risk Management > Compliance > /compliance-software/
115. 5.3 > Compliance & Risk Management > Corrective and Preventive Action (CAPA) > /corrective-and-preventive-action-software/
116. 5.4 > Compliance & Risk Management > GDPR Compliance > /gdpr-compliance-software/
117. 5.5 > Compliance & Risk Management > GRC > /grc-software/
118. 5.6 > Compliance & Risk Management > Integrated Risk Management > /integrated-risk-management-software/
119. 5.7 > Compliance & Risk Management > IT Asset Management > /it-asset-management-software/
120. 5.8 > Compliance & Risk Management > License Management > /license-management-software/
121. 5.9 > Compliance & Risk Management > PCI Compliance > /pci-compliance-software/
122. 5.10 > Compliance & Risk Management > Risk Management > /risk-management-software/
123. 6.0 > Construction > 3D Architecture > /3d-architecture-software/
124. 6.1 > Construction > 3D CAD > /3d-cad-software/
125. 6.2 > Construction > Architectural CAD > /architectural-cad-software/
126. 6.3 > Construction > Architecture > /architecture-software/
127. 6.4 > Construction > Construction Accounting > /construction-accounting-software/
128. 6.5 > Construction > Construction Bid Management > /construction-bid-management-software/
129. 6.6 > Construction > Construction CRM > /construction-crm-software/
130. 6.7 > Construction > Construction Estimating > /construction-estimating-software/
131. 6.8 > Construction > Construction Management > /construction-management-software/
132. 6.9 > Construction > Construction Scheduling > /construction-scheduling-software/
133. 6.10 > Construction > Contractor Management > /contractor-management-software/
134. 6.11 > Construction > Home Builder > /home-builder-software/
135. 6.12 > Construction > Punch List > /punch-list-software/
136. 6.13 > Construction > Remodeling Estimating > /remodeling-estimating-software/
137. 6.14 > Construction > Residential Construction Estimating > /residential-construction-estimating-software/
138. 6.15 > Construction > Takeoff > /takeoff-software/
139. 7.0 > Content & Document > Archiving > /archiving-software/
140. 7.1 > Content & Document > Blog > /blog-software/
141. 7.2 > Content & Document > Content Management > /content-management-software/
142. 7.3 > Content & Document > Digital Asset Management > /digital-asset-management-software/
143. 7.4 > Content & Document > Digital Signage > /digital-signage-software/
144. 7.5 > Content & Document > Digital Signature > /digital-signature-software/
145. 7.6 > Content & Document > Directory > /directory-software/
146. 7.7 > Content & Document > Document Control > /document-control-software/
147. 7.8 > Content & Document > Document Generation > /document-generation-software/
148. 7.9 > Content & Document > Document Management > /document-management-software/
149. 7.10 > Content & Document > Document Version Control > /document-version-control-software/
150. 7.11 > Content & Document > Enterprise Content Management > /enterprise-content-management-software/
151. 7.12 > Content & Document > Enterprise Search > /enterprise-search-software/
152. 7.13 > Content & Document > File Sharing > /file-sharing-software/
153. 7.14 > Content & Document > File Sync > /file-sync-software/
154. 7.15 > Content & Document > Forms Automation > /forms-automation-software/
155. 7.16 > Content & Document > Mobile Content Management > /mobile-content-management-system-software/
156. 7.17 > Content & Document > OCR > /ocr-software/
157. 7.18 > Content & Document > PDF > /pdf-software/
158. 7.19 > Content & Document > Proofreading > /proofreading-software/
159. 7.20 > Content & Document > SEO > /seo-software/
160. 7.21 > Content & Document > Visual Search > /visual-search-software/
161. 7.22 > Content & Document > Waiver > /waiver-software/
162. 7.23 > Content & Document > Web to Print > /web-to-print-software/
163. 8.0 > Customer Management > Call Center > /call-center-software/
164. 8.1 > Customer Management > Complaint Management > /complaint-management-software/
165. 8.2 > Customer Management > Contact Management > /contact-management-software/
166. 8.3 > Customer Management > Customer Communications Management > /customer-communications-management-software/
167. 8.4 > Customer Management > Customer Engagement > /customer-engagement-software/
168. 8.5 > Customer Management > Customer Experience > /customer-experience-software/
169. 8.6 > Customer Management > Customer Reference Management > /customer-reference-management-software/
170. 8.7 > Customer Management > Customer Relationship Management > /customer-relationship-management-software/
171. 8.8 > Customer Management > Customer Satisfaction > /customer-satisfaction-software/
172. 8.9 > Customer Management > Customer Service > /customer-service-software/
173. 8.10 > Customer Management > Customer Success > /customer-success-software/
174. 8.11 > Customer Management > Digital Adoption Platform > /digital-adoption-platform-software/
175. 8.12 > Customer Management > Help Desk > /help-desk-software/
176. 8.13 > Customer Management > Incident Management > /incident-management-software/
177. 8.14 > Customer Management > Knowledge Management > /knowledge-management-software/
178. 8.15 > Customer Management > Live Chat > /live-chat-software/
179. 8.16 > Customer Management > Mac CRM > /mac-crm-software/
180. 8.17 > Customer Management > Nonprofit CRM > /nonprofit-crm-software/
181. 8.18 > Customer Management > Online CRM > /online-crm-software/
182. 8.19 > Customer Management > Service Desk > /service-desk-software/
183. 8.20 > Customer Management > Small Business CRM > /small-business-crm-software/
184. 8.21 > Customer Management > Social CRM Tools > /social-crm-tools-software/
185. 9.0 > Data Management > Big Data > /big-data-software/
186. 9.1 > Data Management > Business Continuity > /business-continuity-software/
187. 9.2 > Data Management > Data Analysis > /data-analysis-software/
188. 9.3 > Data Management > Data Center Management > /data-center-management-software/
189. 9.4 > Data Management > Data Discovery > /data-discovery-software/
190. 9.5 > Data Management > Data Entry > /data-entry-software/
191. 9.6 > Data Management > Data Extraction > /data-extraction-software/
192. 9.7 > Data Management > Data Governance > /data-governance-software/
193. 9.8 > Data Management > Data Management > /data-management-software/
194. 9.9 > Data Management > Data Mining > /data-mining-software/
195. 9.10 > Data Management > Data Quality > /data-quality-software/
196. 9.11 > Data Management > Data Visualization > /data-visualization-software/
197. 9.12 > Data Management > Data Warehouse > /data-warehouse-software/
198. 9.13 > Data Management > Database Management > /database-management-software/
199. 9.14 > Data Management > Database Monitoring > /database-monitoring-software/
200. 9.15 > Data Management > EDI > /edi-software/
201. 9.16 > Data Management > Electronic Data Capture > /electronic-data-capture-software/
202. 9.17 > Data Management > Email Archiving  > /email-archiving-software/
203. 9.18 > Data Management > Email Management > /email-management-software/
204. 9.19 > Data Management > Email Signature > /email-signature-software/
205. 9.20 > Data Management > Embedded Analytics > /embedded-analytics-software/
206. 9.21 > Data Management > ETL > /etl-software/
207. 9.22 > Data Management > Master Data Management > /master-data-management-software/
208. 9.23 > Data Management > Mobile Analytics > /mobile-analytics-software/
209. 9.24 > Data Management > Portal > /portal-software/
210. 9.25 > Data Management > Predictive Analytics > /predictive-analytics-software/
211. 9.26 > Data Management > Qualitative Data Analysis > /qualitative-data-analysis-software/
212. 9.27 > Data Management > RDBMS > /rdbms-software/
213. 9.28 > Data Management > Text Mining > /text-mining-software/
214. 9.29 > Data Management > Virtual Data Room > /virtual-data-room-software/
215. 9.30 > Data Management > Web Analytics > /web-analytics-software/
216. 10.0 > Education & eLearning > Admissions > /admissions-software/
217. 10.1 > Education & eLearning > Alumni Management > /alumni-management-software/
218. 10.2 > Education & eLearning > Assessment > /assessment-software/
219. 10.3 > Education & eLearning > Child Care > /child-care-software/
220. 10.4 > Education & eLearning > Class Registration > /class-registration-software/
221. 10.5 > Education & eLearning > Classroom Management > /classroom-management-software/
222. 10.6 > Education & eLearning > Course Authoring > /course-authoring-software/
223. 10.7 > Education & eLearning > eLearning Authoring Tools > /elearning-authoring-tools-software/
224. 10.8 > Education & eLearning > Exam > /exam-software/
225. 10.9 > Education & eLearning > Gradebook > /gradebook-software/
226. 10.10 > Education & eLearning > Higher Education > /higher-education-software/
227. 10.11 > Education & eLearning > K-12 > /k-12-software/
228. 10.12 > Education & eLearning > Learning Experience Platform (LEP) > /learning-experience-platform-software/
229. 10.13 > Education & eLearning > Learning Management System > /learning-management-system-software/
230. 10.14 > Education & eLearning > Library Automation > /library-automation-software/
231. 10.15 > Education & eLearning > Microlearning > /microlearning-software/
232. 10.16 > Education & eLearning > Mobile Learning > /mobile-learning-software/
233. 10.17 > Education & eLearning > Music School > /music-school-software/
234. 10.18 > Education & eLearning > Scholarship Management > /scholarship-management-software/
235. 10.19 > Education & eLearning > School Accounting > /school-accounting-software/
236. 10.20 > Education & eLearning > School Administration > /school-administration-software/
237. 10.21 > Education & eLearning > Student Engagement Platform > /student-engagement-platform-software/
238. 10.22 > Education & eLearning > Student Information System > /student-information-system-software/
239. 10.23 > Education & eLearning > Training > /training-software/
240. 10.24 > Education & eLearning > Tutoring > /tutoring-software/
241. 10.25 > Education & eLearning > Virtual Classroom > /virtual-classroom-software/
242. 10.26 > Education & eLearning > Whiteboard > /whiteboard-software/
243. 11.0 > Energy & Environment > EHS Management > /ehs-management-software/
244. 11.1 > Energy & Environment > Emissions Management > /emissions-management-software/
245. 11.2 > Energy & Environment > Energy Management > /energy-management-software/
246. 11.3 > Energy & Environment > Environmental > /environmental-software/
247. 11.4 > Energy & Environment > Forestry > /forestry-software/
248. 11.5 > Energy & Environment > GIS > /gis-software/
249. 11.6 > Energy & Environment > Land Management > /land-management-software/
250. 11.7 > Energy & Environment > Mining > /mining-software/
251. 11.8 > Energy & Environment > Oil and Gas > /oil-and-gas-software/
252. 11.9 > Energy & Environment > Safety Management > /safety-management-software/
253. 11.10 > Energy & Environment > Sustainability > /sustainability-software/
254. 11.11 > Energy & Environment > Utility Billing > /utility-billing-software/
255. 11.12 > Energy & Environment > Utility Management Systems > /utility-management-systems-software/
256. 12.0 > Event > Audience Response > /audience-response-software/
257. 12.1 > Event > Conference > /conference-software/
258. 12.2 > Event > Event Booking > /event-booking-software/
259. 12.3 > Event > Event Check In > /event-check-in-software/
260. 12.4 > Event > Event Management > /event-management-software/
261. 12.5 > Event > Event Marketing > /event-marketing-software/
262. 12.6 > Event > Festival Management > /festival-management-software/
263. 12.7 > Event > Live Streaming > /live-streaming-software/
264. 12.8 > Event > Meeting > /meeting-software/
265. 12.9 > Event > Mobile Event Apps > /mobile-event-apps-software/
266. 12.10 > Event > Registration > /registration-software/
267. 12.11 > Event > Ticketing > /ticketing-software/
268. 12.12 > Event > Venue Management > /venue-management-software/
269. 12.13 > Event > Virtual Event > /virtual-event-software/
270. 13.0 > Facility > Appointment Reminder > /appointment-reminder-software/
271. 13.1 > Facility > Appointment Scheduling > /appointment-scheduling-software/
272. 13.2 > Facility > Facility Management > /facility-management-software/
273. 13.3 > Facility > IWMS > /iwms-software/
274. 13.4 > Facility > Key Management > /key-management-software/
275. 13.5 > Facility > Mailroom Management > /mailroom-management-software/
276. 13.6 > Facility > Meeting Room Booking > /meeting-room-booking-system-software/
277. 13.7 > Facility > Physical Security > /physical-security-software/
278. 13.8 > Facility > Scheduling > /scheduling-software/
279. 13.9 > Facility > Space Management > /space-management-software/
280. 13.10 > Facility > Visitor Management > /visitor-management-software/
281. 13.11 > Facility > Waitlist > /waitlist-software/
282. 14.0 > Field Service > Arborist > /arborist-software/
283. 14.1 > Field Service > Carpet Cleaning > /carpet-cleaning-software/
284. 14.2 > Field Service > Electrical Contractor > /electrical-contractor-software/
285. 14.3 > Field Service > Electrical Estimating > /electrical-estimating-software/
286. 14.4 > Field Service > Field Service Management > /field-service-management-software/
287. 14.5 > Field Service > Garage Door > /garage-door-software/
288. 14.6 > Field Service > Handyman > /handyman-software/
289. 14.7 > Field Service > Home Inspection > /home-inspection-software/
290. 14.8 > Field Service > HVAC > /hvac-software/
291. 14.9 > Field Service > HVAC Estimating > /hvac-estimating-software/
292. 14.10 > Field Service > Inspection > /inspection-software/
293. 14.11 > Field Service > IT Service > /it-service-software/
294. 14.12 > Field Service > Janitorial > /janitorial-software/
295. 14.13 > Field Service > Landscape > /landscape-software/
296. 14.14 > Field Service > Lawn Care > /lawn-care-software/
297. 14.15 > Field Service > Maid Service > /maid-service-software/
298. 14.16 > Field Service > Pest Control > /pest-control-software/
299. 14.17 > Field Service > Plumbing > /plumbing-software/
300. 14.18 > Field Service > Plumbing Estimating > /plumbing-estimating-software/
301. 14.19 > Field Service > Recycling > /recycling-software/
302. 14.20 > Field Service > Roofing > /roofing-software/
303. 14.21 > Field Service > Security System Installer > /security-system-installer-software/
304. 14.22 > Field Service > Service Dispatch > /service-dispatch-software/
305. 14.23 > Field Service > Waste Management > /waste-management-software/
306. 14.24 > Field Service > Work Order > /work-order-software/
307. 15.0 > Food Service > Bakery > /bakery-software/
308. 15.1 > Food Service > Bar POS > /bar-pos-software/
309. 15.2 > Food Service > Brewery > /brewery-software/
310. 15.3 > Food Service > Catering > /catering-software/
311. 15.4 > Food Service > Food Costing > /food-costing-software/
312. 15.5 > Food Service > Food Delivery > /food-delivery-software/
313. 15.6 > Food Service > Food Service Distribution > /food-service-distribution-software/
314. 15.7 > Food Service > Food Service Management > /food-service-management-software/
315. 15.8 > Food Service > Food Traceability > /food-traceability-software/
316. 15.9 > Food Service > Restaurant Management > /restaurant-management-software/
317. 15.10 > Food Service > Restaurant POS > /restaurant-pos-software/
318. 16.0 > Healthcare & Medical > Applied Behavior Analysis > /applied-behavior-analysis-software/
319. 16.1 > Healthcare & Medical > Assisted Living > /assisted-living-software/
320. 16.2 > Healthcare & Medical > Chiropractic > /chiropractic-software/
321. 16.3 > Healthcare & Medical > Clinical Trial Management > /clinical-trial-management-software/
322. 16.4 > Healthcare & Medical > Credentialing > /credentialing-software/
323. 16.5 > Healthcare & Medical > Dental > /dental-software/
324. 16.6 > Healthcare & Medical > Dental Charting > /dental-charting-software/
325. 16.7 > Healthcare & Medical > Dental Imaging > /dental-imaging-software/
326. 16.8 > Healthcare & Medical > Dermatology > /dermatology-software/
327. 16.9 > Healthcare & Medical > e-Prescribing > /eprescribing-software/
328. 16.10 > Healthcare & Medical > Electronic Medical Records > /electronic-medical-records-software/
329. 16.11 > Healthcare & Medical > EMS > /ems-software/
330. 16.12 > Healthcare & Medical > Healthcare CRM > /healthcare-crm-software/
331. 16.13 > Healthcare & Medical > HIPAA Compliance > /hipaa-compliance-software/
332. 16.14 > Healthcare & Medical > Home Care > /home-care-software/
333. 16.15 > Healthcare & Medical > Home Health Care > /home-health-care-software/
334. 16.16 > Healthcare & Medical > Hospice > /hospice-software/
335. 16.17 > Healthcare & Medical > Hospital Management > /hospital-management-software/
336. 16.18 > Healthcare & Medical > Laboratory Information Management System > /laboratory-information-management-system-software/
337. 16.19 > Healthcare & Medical > Long Term Care > /long-term-care-software/
338. 16.20 > Healthcare & Medical > Massage Therapy > /massage-therapy-software/
339. 16.21 > Healthcare & Medical > Medical Billing > /medical-billing-software/
340. 16.22 > Healthcare & Medical > Medical Imaging > /medical-imaging-software/
341. 16.23 > Healthcare & Medical > Medical Inventory > /medical-inventory-software/
342. 16.24 > Healthcare & Medical > Medical Lab > /medical-lab-software/
343. 16.25 > Healthcare & Medical > Medical Practice Management > /medical-practice-management-software/
344. 16.26 > Healthcare & Medical > Medical Scheduling > /medical-scheduling-software/
345. 16.27 > Healthcare & Medical > Medical Spa > /medical-spa-software/
346. 16.28 > Healthcare & Medical > Medical Transcription > /medical-transcription-software/
347. 16.29 > Healthcare & Medical > Mental Health > /mental-health-software/
348. 16.30 > Healthcare & Medical > Nurse Scheduling > /nurse-scheduling-software/
349. 16.31 > Healthcare & Medical > Nursing Home > /nursing-home-software/
350. 16.32 > Healthcare & Medical > Occupational Therapy > /occupational-therapy-software/
351. 16.33 > Healthcare & Medical > Optometry > /optometry-software/
352. 16.34 > Healthcare & Medical > PACS > /pacs-software/
353. 16.35 > Healthcare & Medical > Patient Case Management > /patient-case-management-software/
354. 16.36 > Healthcare & Medical > Patient Engagement > /patient-engagement-software/
355. 16.37 > Healthcare & Medical > Patient Management > /patient-management-software/
356. 16.38 > Healthcare & Medical > Patient Portal > /patient-portal-software/
357. 16.39 > Healthcare & Medical > Pediatric > /pediatric-software/
358. 16.40 > Healthcare & Medical > Pharmacy > /pharmacy-software/
359. 16.41 > Healthcare & Medical > Physical Therapy > /physical-therapy-software/
360. 16.42 > Healthcare & Medical > Plastic Surgery > /plastic-surgery-software/
361. 16.43 > Healthcare & Medical > Podiatry > /podiatry-software/
362. 16.44 > Healthcare & Medical > Radiology > /radiology-software/
363. 16.45 > Healthcare & Medical > Remote Patient Monitoring > /remote-patient-monitoring-software/
364. 16.46 > Healthcare & Medical > Speech Therapy > /speech-therapy-software/
365. 16.47 > Healthcare & Medical > Telemedicine > /telemedicine-software/
366. 17.0 > Hospitality & Travel > Airline Reservation System > /airline-reservation-system-software/
367. 17.1 > Hospitality & Travel > Hospitality Property Management > /hospitality-property-management-software/
368. 17.2 > Hospitality & Travel > Hostel Management > /hostel-management-software/
369. 17.3 > Hospitality & Travel > Hotel Channel Management > /hotel-channel-management-software/
370. 17.4 > Hospitality & Travel > Reservations > /reservations-software/
371. 17.5 > Hospitality & Travel > Spa > /spa-software/
372. 17.6 > Hospitality & Travel > Timeshare > /timeshare-software/
373. 17.7 > Hospitality & Travel > Tour Operator > /tour-operator-software/
374. 17.8 > Hospitality & Travel > Travel Agency > /travel-agency-software/
375. 17.9 > Hospitality & Travel > Travel Management > /travel-management-software/
376. 17.10 > Hospitality & Travel > Vacation Rental > /vacation-rental-software/
377. 18.0 > HR & Talent > 360 Degree Feedback > /360-degree-feedback-software/
378. 18.1 > HR & Talent > Applicant Tracking > /applicant-tracking-software/
379. 18.2 > HR & Talent > Attendance Tracking > /attendance-tracking-software/
380. 18.3 > HR & Talent > Background Check > /background-check-software/
381. 18.4 > HR & Talent > Benefits Administration > /benefits-administration-software/
382. 18.5 > HR & Talent > Business Card > /business-card-software/
383. 18.6 > HR & Talent > Coaching > /coaching-software/
384. 18.7 > HR & Talent > Compensation Management > /compensation-management-software/
385. 18.8 > HR & Talent > Corporate Wellness > /corporate-wellness-software/
386. 18.9 > HR & Talent > Employee Communication Tools > /employee-communication-tools-software/
387. 18.10 > HR & Talent > Employee Engagement > /employee-engagement-software/
388. 18.11 > HR & Talent > Employee Monitoring > /employee-monitoring-software/
389. 18.12 > HR & Talent > Employee Recognition > /employee-recognition-software/
390. 18.13 > HR & Talent > Employee Scheduling > /employee-scheduling-software/
391. 18.14 > HR & Talent > HR Analytics > /hr-analytics-software/
392. 18.15 > HR & Talent > Human Resource > /human-resource-software/
393. 18.16 > HR & Talent > Job Board > /job-board-software/
394. 18.17 > HR & Talent > Job Evaluation > /job-evaluation-software/
395. 18.18 > HR & Talent > Leave Management System > /leave-management-system-software/
396. 18.19 > HR & Talent > Mentoring > /mentoring-software/
397. 18.20 > HR & Talent > Onboarding > /onboarding-software/
398. 18.21 > HR & Talent > Org Chart > /org-chart-software/
399. 18.22 > HR & Talent > Payroll > /payroll-software/
400. 18.23 > HR & Talent > Performance Appraisal > /performance-appraisal-software/
401. 18.24 > HR & Talent > Pre-employment Testing > /pre-employment-testing-software/
402. 18.25 > HR & Talent > Recruiting > /recruiting-software/
403. 18.26 > HR & Talent > Recruiting Agency > /recruiting-agency-software/
404. 18.27 > HR & Talent > Reference Check > /reference-check-software/
405. 18.28 > HR & Talent > Relocation > /relocation-software/
406. 18.29 > HR & Talent > Staffing Agency > /staffing-agency-software/
407. 18.30 > HR & Talent > Succession Planning > /succession-planning-software/
408. 18.31 > HR & Talent > Talent Management > /talent-management-software/
409. 18.32 > HR & Talent > Time Clock > /time-clock-software/
410. 18.33 > HR & Talent > Video Interviewing > /video-interviewing-software/
411. 18.34 > HR & Talent > Workforce Management > /workforce-management-software/
412. 19.0 > Insurance > Claims Processing > /claims-processing-software/
413. 19.1 > Insurance > Commercial Insurance > /commercial-insurance-software/
414. 19.2 > Insurance > Insurance Agency > /insurance-agency-software/
415. 19.3 > Insurance > Insurance Policy > /insurance-policy-software/
416. 19.4 > Insurance > Insurance Rating > /insurance-rating-software/
417. 19.5 > Insurance > P&C Insurance > /p-c-insurance-software/
418. 20.0 > IT & Development > API Management > /api-management-software/
419. 20.1 > IT & Development > App Building > /app-building-software/
420. 20.2 > IT & Development > App Design > /app-design-software/
421. 20.3 > IT & Development > Application Development > /application-development-software/
422. 20.4 > IT & Development > Application Lifecycle Management > /application-lifecycle-management-software/
423. 20.5 > IT & Development > Application Performance Management > /application-performance-management-software/
424. 20.6 > IT & Development > Artificial Intelligence > /artificial-intelligence-software/
425. 20.7 > IT & Development > Augmented Reality > /augmented-reality-software/
426. 20.8 > IT & Development > Automated Testing > /automated-testing-software/
427. 20.9 > IT & Development > Backup > /backup-software/
428. 20.10 > IT & Development > Change Management > /change-management-software/
429. 20.11 > IT & Development > Cloud Management > /cloud-management-software/
430. 20.12 > IT & Development > Cloud Storage > /cloud-storage-software/
431. 20.13 > IT & Development > CMDB > /cmdb-software/
432. 20.14 > IT & Development > Continuous Integration > /continuous-integration-software/
433. 20.15 > IT & Development > Conversational AI > /conversational-ai-platform-software/
434. 20.16 > IT & Development > Data Loss Prevention > /data-loss-prevention-software/
435. 20.17 > IT & Development > Deep Learning > /deep-learning-software/
436. 20.18 > IT & Development > DevOps > /devops-software/
437. 20.19 > IT & Development > Disk Imaging > /disk-imaging-software/
438. 20.20 > IT & Development > Enterprise Architecture > /enterprise-architecture-software/
439. 20.21 > IT & Development > Game Development > /game-development-software/
440. 20.22 > IT & Development > Identity Management > /identity-management-software/
441. 20.23 > IT & Development > Infrastructure as a Service (IaaS) > /infrastructure-as-a-service-solutions-software/
442. 20.24 > IT & Development > Integration > /integration-software/
443. 20.25 > IT & Development > Intranet > /intranet-software/
444. 20.26 > IT & Development > IoT > /iot-software/
445. 20.27 > IT & Development > IT Management > /it-management-software/
446. 20.28 > IT & Development > ITSM > /itsm-software/
447. 20.29 > IT & Development > Java CMS > /java-cms-software/
448. 20.30 > IT & Development > Load Balancing > /load-balancing-software/
449. 20.31 > IT & Development > Log Management > /log-management-software/
450. 20.32 > IT & Development > Logbook > /logbook-software/
451. 20.33 > IT & Development > Low Code Development Platform > /low-code-development-platform-software/
452. 20.34 > IT & Development > Machine Learning > /machine-learning-software/
453. 20.35 > IT & Development > Mobility > /mobility-software/
454. 20.36 > IT & Development > MSP > /msp-software/
455. 20.37 > IT & Development > Network Mapping > /network-mapping-software/
456. 20.38 > IT & Development > Network Monitoring > /network-monitoring-software/
457. 20.39 > IT & Development > Network Troubleshooting > /network-troubleshooting-software/
458. 20.40 > IT & Development > Patch Management > /patch-management-software/
459. 20.41 > IT & Development > Performance Testing > /performance-testing-software/
460. 20.42 > IT & Development > Remote Desktop > /remote-desktop-software/
461. 20.43 > IT & Development > Remote Monitoring and Management > /remote-monitoring-and-management-software/
462. 20.44 > IT & Development > Remote Support > /remote-support-software/
463. 20.45 > IT & Development > Robotic Process Automation (RPA) > /robotic-process-automation-software/
464. 20.46 > IT & Development > SaaS Management > /saas-management-software/
465. 20.47 > IT & Development > Server Backup > /server-backup-software/
466. 20.48 > IT & Development > Server Management > /server-management-software/
467. 20.49 > IT & Development > Source Code Management > /source-code-management-software/
468. 20.50 > IT & Development > VDI > /vdi-software/
469. 20.51 > IT & Development > Virtual Machine > /virtual-machine-software/
470. 20.52 > IT & Development > Virtualization > /virtualization-software/
471. 20.53 > IT & Development > VPN > /vpn-software/
472. 20.54 > IT & Development > VR > /vr-software/
473. 20.55 > IT & Development > Website Builder > /website-builder-software/
474. 20.56 > IT & Development > Website Monitoring > /website-monitoring-software/
475. 20.57 > IT & Development > Website Optimization Tools > /website-optimization-tools-software/
476. 21.0 > IT Security > Anti-spam > /anti-spam-software/
477. 21.1 > IT Security > Authentication > /authentication-software/
478. 21.2 > IT Security > Cloud Security > /cloud-security-software/
479. 21.3 > IT Security > Computer Security > /computer-security-software/
480. 21.4 > IT Security > Cybersecurity > /cybersecurity-software/
481. 21.5 > IT Security > Email Security > /email-security-software/
482. 21.6 > IT Security > Endpoint Detection and Response (EDR) > /endpoint-detection-and-response-software/
483. 21.7 > IT Security > Endpoint Protection > /endpoint-protection-software/
484. 21.8 > IT Security > Network Security > /network-security-software/
485. 21.9 > IT Security > Password Management > /password-management-software/
486. 21.10 > IT Security > Privileged Access Management > /privileged-access-management-software/
487. 21.11 > IT Security > SIEM > /siem-software/
488. 21.12 > IT Security > Single Sign On (SSO) > /single-sign-on-software/
489. 21.13 > IT Security > Vulnerability Management > /vulnerability-management-software/
490. 22.0 > Legal & Law Enforcement > Conflict Checking > /conflict-checking-software/
491. 22.1 > Legal & Law Enforcement > Court Management > /court-management-software/
492. 22.2 > Legal & Law Enforcement > Digital Rights Management > /digital-rights-management-software/
493. 22.3 > Legal & Law Enforcement > Docketing > /docketing-software/
494. 22.4 > Legal & Law Enforcement > Electronic Discovery > /electronic-discovery-software/
495. 22.5 > Legal & Law Enforcement > Emergency Notification > /emergency-notification-software/
496. 22.6 > Legal & Law Enforcement > Entity Management > /entity-management-software/
497. 22.7 > Legal & Law Enforcement > Intellectual Property Management > /intellectual-property-management-software/
498. 22.8 > Legal & Law Enforcement > Investigation Management > /investigation-management-software/
499. 22.9 > Legal & Law Enforcement > Jail Management > /jail-management-software/
500. 22.10 > Legal & Law Enforcement > Law Enforcement > /law-enforcement-software/
501. 22.11 > Legal & Law Enforcement > Law Practice Management > /law-practice-management-software/
502. 22.12 > Legal & Law Enforcement > Legal Billing > /legal-billing-software/
503. 22.13 > Legal & Law Enforcement > Legal Calendar > /legal-calendar-software/
504. 22.14 > Legal & Law Enforcement > Legal Case Management > /legal-case-management-software/
505. 22.15 > Legal & Law Enforcement > Legal Document Management > /legal-document-management-software/
506. 22.16 > Legal & Law Enforcement > Legal Research > /legal-research-software/
507. 22.17 > Legal & Law Enforcement > Trust Accounting > /trust-accounting-software/
508. 23.0 > Logistics & Supply Chain >  Shipping > /shipping-software/
509. 23.1 > Logistics & Supply Chain > Barcoding > /barcoding-software/
510. 23.2 > Logistics & Supply Chain > Courier > /courier-software/
511. 23.3 > Logistics & Supply Chain > Delivery Management > /delivery-management-software/
512. 23.4 > Logistics & Supply Chain > Demand Planning > /demand-planning-software/
513. 23.5 > Logistics & Supply Chain > Distribution > /distribution-software/
514. 23.6 > Logistics & Supply Chain > Dock Scheduling > /dock-scheduling-software/
515. 23.7 > Logistics & Supply Chain > Dropshipping > /dropshipping-software/
516. 23.8 > Logistics & Supply Chain > Fleet Maintenance > /fleet-maintenance-software/
517. 23.9 > Logistics & Supply Chain > Fleet Management > /fleet-management-software/
518. 23.10 > Logistics & Supply Chain > Freight > /freight-software/
519. 23.11 > Logistics & Supply Chain > Fuel Management > /fuel-management-software/
520. 23.12 > Logistics & Supply Chain > GPS Tracking > /gps-tracking-software/
521. 23.13 > Logistics & Supply Chain > Inventory Management > /inventory-management-software/
522. 23.14 > Logistics & Supply Chain > Logistics > /logistics-software/
523. 23.15 > Logistics & Supply Chain > Marine > /marine-software/
524. 23.16 > Logistics & Supply Chain > Moving > /moving-software/
525. 23.17 > Logistics & Supply Chain > Packaging > /packaging-software/
526. 23.18 > Logistics & Supply Chain > Parcel Audit > /parcel-audit-software/
527. 23.19 > Logistics & Supply Chain > Parking Management > /parking-management-software/
528. 23.20 > Logistics & Supply Chain > Public Transportation > /public-transportation-software/
529. 23.21 > Logistics & Supply Chain > Route Planning > /route-planning-software/
530. 23.22 > Logistics & Supply Chain > School Bus Routing > /school-bus-routing-software/
531. 23.23 > Logistics & Supply Chain > Shipment Tracking > /shipment-tracking-software/
532. 23.24 > Logistics & Supply Chain > Supply Chain Management > /supply-chain-management-software/
533. 23.25 > Logistics & Supply Chain > Towing > /towing-software/
534. 23.26 > Logistics & Supply Chain > Transportation Dispatch > /transportation-dispatch-software/
535. 23.27 > Logistics & Supply Chain > Transportation Management > /transportation-management-software/
536. 23.28 > Logistics & Supply Chain > Trucking > /trucking-software/
537. 23.29 > Logistics & Supply Chain > Vendor Management > /vendor-management-software/
538. 23.30 > Logistics & Supply Chain > Warehouse Management > /warehouse-management-software/
539. 23.31 > Logistics & Supply Chain > Yard Management > /yard-management-software/
540. 24.0 > Maintenance > Auto Body > /auto-body-software/
541. 24.1 > Maintenance > Auto Repair > /auto-repair-software/
542. 24.2 > Maintenance > Aviation Maintenance > /aviation-maintenance-software/
543. 24.3 > Maintenance > Building Maintenance > /building-maintenance-software/
544. 24.4 > Maintenance > CMMS > /cmms-software/
545. 24.5 > Maintenance > Equipment Maintenance > /equipment-maintenance-software/
546. 24.6 > Maintenance > Maintenance Management > /maintenance-management-software/
547. 24.7 > Maintenance > Preventive Maintenance > /preventive-maintenance-software/
548. 24.8 > Maintenance > Tool Management > /tool-management-software/
549. 25.0 > Manufacturing & Engineering > BIM > /bim-software/
550. 25.1 > Manufacturing & Engineering > Calibration Management > /calibration-management-software/
551. 25.2 > Manufacturing & Engineering > Chemical > /chemical-software/
552. 25.3 > Manufacturing & Engineering > Electrical Design > /electrical-design-software/
553. 25.4 > Manufacturing & Engineering > Engineering CAD > /engineering-cad-software/
554. 25.5 > Manufacturing & Engineering > Job Shop > /job-shop-software/
555. 25.6 > Manufacturing & Engineering > Manufacturing > /manufacturing-execution-software/
556. 25.7 > Manufacturing & Engineering > Manufacturing Execution > /manufacturing-execution-software/
557. 25.8 > Manufacturing & Engineering > MRP > /mrp-software/
558. 25.9 > Manufacturing & Engineering > OEE > /oee-software/
559. 25.10 > Manufacturing & Engineering > Product Configurator > /product-configurator-software/
560. 25.11 > Manufacturing & Engineering > Product Data Management > /product-data-management-software/
561. 25.12 > Manufacturing & Engineering > Production Scheduling > /production-scheduling-software/
562. 25.13 > Manufacturing & Engineering > Quality Management > /quality-management-software/
563. 25.14 > Manufacturing & Engineering > SCADA > /scada-software/
564. 25.15 > Manufacturing & Engineering > Simulation > /simulation-software/
565. 25.16 > Manufacturing & Engineering > SPC > /spc-software/
566. 26.0 > Marketing & Digital Marketing > Account Based Marketing > /account-based-marketing-software/
567. 26.1 > Marketing & Digital Marketing > Ad Server > /ad-server-software/
568. 26.2 > Marketing & Digital Marketing > Advertising Agency > /advertising-agency-software/
569. 26.3 > Marketing & Digital Marketing > Affiliate > /affiliate-software/
570. 26.4 > Marketing & Digital Marketing > App Store Optimization Tools (ASO) > /app-store-optimization-tools-software/
571. 26.5 > Marketing & Digital Marketing > Brand Management > /brand-management-software/
572. 26.6 > Marketing & Digital Marketing > Brand Protection > /brand-protection-software/
573. 26.7 > Marketing & Digital Marketing > Campaign Management > /campaign-management-software/
574. 26.8 > Marketing & Digital Marketing > Click Fraud > /click-fraud-software/
575. 26.9 > Marketing & Digital Marketing > Content Marketing > /content-marketing-software/
576. 26.10 > Marketing & Digital Marketing > Contest > /contest-software/
577. 26.11 > Marketing & Digital Marketing > Conversational Marketing Platform > /conversational-marketing-platform-software/
578. 26.12 > Marketing & Digital Marketing > Customer Data Platform > /customer-data-platform-software/
579. 26.13 > Marketing & Digital Marketing > Direct Mail Automation > /direct-mail-automation-software/
580. 26.14 > Marketing & Digital Marketing > Email Marketing > /email-marketing-software/
581. 26.15 > Marketing & Digital Marketing > Email Tracking > /email-tracking-software/
582. 26.16 > Marketing & Digital Marketing > Email Verification Tools > /email-verification-tools-software/
583. 26.17 > Marketing & Digital Marketing > Influencer Marketing > /influencer-marketing-software/
584. 26.18 > Marketing & Digital Marketing > Landing Page > /landing-page-software/
585. 26.19 > Marketing & Digital Marketing > Lead Generation > /lead-generation-software/
586. 26.20 > Marketing & Digital Marketing > Link Management Tools > /link-management-tools-software/
587. 26.21 > Marketing & Digital Marketing > Market Research > /market-research-software/
588. 26.22 > Marketing & Digital Marketing > Marketing Analytics > /marketing-analytics-software/
589. 26.23 > Marketing & Digital Marketing > Marketing Attribution > /marketing-attribution-software/
590. 26.24 > Marketing & Digital Marketing > Marketing Automation > /marketing-automation-software/
591. 26.25 > Marketing & Digital Marketing > Marketing Planning > /marketing-planning-software/
592. 26.26 > Marketing & Digital Marketing > Mobile Marketing > /mobile-marketing-software/
593. 26.27 > Marketing & Digital Marketing > MRM > /mrm-software/
594. 26.28 > Marketing & Digital Marketing > Online Proofing > /online-proofing-software/
595. 26.29 > Marketing & Digital Marketing > Personalization > /personalization-software/
596. 26.30 > Marketing & Digital Marketing > PPC > /ppc-software/
597. 26.31 > Marketing & Digital Marketing > Public Relations > /public-relations-software/
598. 26.32 > Marketing & Digital Marketing > Push Notifications > /push-notifications-software/
599. 26.33 > Marketing & Digital Marketing > Reputation Management > /reputation-management-software/
600. 26.34 > Marketing & Digital Marketing > Retargeting > /retargeting-software/
601. 26.35 > Marketing & Digital Marketing > Review Management > /review-management-software/
602. 26.36 > Marketing & Digital Marketing > SMS Marketing > /sms-marketing-software/
603. 26.37 > Marketing & Digital Marketing > Social Media Analytics Tools > /social-media-analytics-tools-software/
604. 26.38 > Marketing & Digital Marketing > Social Media Management > /social-media-management-software/
605. 26.39 > Marketing & Digital Marketing > Social Media Marketing > /social-media-marketing-software/
606. 26.40 > Marketing & Digital Marketing > Social Media Monitoring > /social-media-monitoring-software/
607. 26.41 > Marketing & Digital Marketing > Social Networking > /social-networking-software/
608. 26.42 > Marketing & Digital Marketing > Social Selling > /social-selling-software/
609. 26.43 > Marketing & Digital Marketing > Survey > /survey-software/
610. 26.44 > Marketing & Digital Marketing > Trade Promotion Management > /trade-promotion-management-software/
611. 26.45 > Marketing & Digital Marketing > Transactional Email > /transactional-email-software/
612. 27.0 > Nonprofit & Public Sector > Advocacy > /advocacy-software/
613. 27.1 > Nonprofit & Public Sector > Association Management > /association-management-software/
614. 27.2 > Nonprofit & Public Sector > Cemetery > /cemetery-software/
615. 27.3 > Nonprofit & Public Sector > Church Accounting > /church-accounting-software/
616. 27.4 > Nonprofit & Public Sector > Church Management > /church-management-software/
617. 27.5 > Nonprofit & Public Sector > Church Presentation > /church-presentation-software/
618. 27.6 > Nonprofit & Public Sector > Code Enforcement > /code-enforcement-software/
619. 27.7 > Nonprofit & Public Sector > Donation Management > /donation-management-software/
620. 27.8 > Nonprofit & Public Sector > Fire Department > /fire-department-software/
621. 27.9 > Nonprofit & Public Sector > Fund Accounting > /fund-accounting-software/
622. 27.10 > Nonprofit & Public Sector > Fundraising > /fundraising-software/
623. 27.11 > Nonprofit & Public Sector > Government > /government-software/
624. 27.12 > Nonprofit & Public Sector > Grant Management > /grant-management-software/
625. 27.13 > Nonprofit & Public Sector > Human Services > /human-services-software/
626. 27.14 > Nonprofit & Public Sector > Membership Management > /membership-management-software/
627. 27.15 > Nonprofit & Public Sector > Municipal > /municipal-software/
628. 27.16 > Nonprofit & Public Sector > Museum > /museum-software/
629. 27.17 > Nonprofit & Public Sector > Nonprofit > /nonprofit-software/
630. 27.18 > Nonprofit & Public Sector > Permit > /permit-software/
631. 27.19 > Nonprofit & Public Sector > Political Campaign > /political-campaign-software/
632. 27.20 > Nonprofit & Public Sector > Polling > /polling-software/
633. 27.21 > Nonprofit & Public Sector > Public Works > /public-works-software/
634. 27.22 > Nonprofit & Public Sector > Social Work Case Management > /social-work-case-management-software/
635. 27.23 > Nonprofit & Public Sector > Volunteer Management > /volunteer-management-software/
636. 27.24 > Nonprofit & Public Sector > Voting > /voting-software/
637. 27.25 > Nonprofit & Public Sector > Worship > /worship-software/
638. 28.0 > Product > AB Testing > /ab-testing-software/
639. 28.1 > Product > Creative Management > /creative-management-software/
640. 28.2 > Product > Customer Journey Mapping Tools > /customer-journey-mapping-tools-software/
641. 28.3 > Product > Gamification > /gamification-software/
642. 28.4 > Product > Graphic Design > /graphic-design-software/
643. 28.5 > Product > Heatmap > /heatmap-software/
644. 28.6 > Product > PIM > /pim-software/
645. 28.7 > Product > Product Lifecycle Management > /product-lifecycle-management-software/
646. 28.8 > Product > Product Management > /product-management-software/
647. 28.9 > Product > Product Roadmap > /product-roadmap-software/
648. 28.10 > Product > Prototyping > /prototyping-software/
649. 28.11 > Product > UX > /ux-software/
650. 28.12 > Product > Vector Graphics > /vector-graphics-software/
651. 28.13 > Product > Wireframe > /wireframe-software/
652. 29.0 > Project Management > Agile Project Management Tools > /agile-project-management-tools-software/
653. 29.1 > Project Management > Bug Tracking > /bug-tracking-software/
654. 29.2 > Project Management > Diagram > /diagram-software/
655. 29.3 > Project Management > Gantt Chart > /gantt-chart-software/
656. 29.4 > Project Management > Idea Management > /idea-management-software/
657. 29.5 > Project Management > Innovation > /innovation-software/
658. 29.6 > Project Management > Issue Tracking > /issue-tracking-software/
659. 29.7 > Project Management > IT Project Management > /it-project-management-software/
660. 29.8 > Project Management > Job Costing > /job-costing-software/
661. 29.9 > Project Management > Kanban Tools > /kanban-tools-software/
662. 29.10 > Project Management > Mind Mapping > /mind-mapping-software/
663. 29.11 > Project Management > Professional Services Automation > /professional-services-automation-software/
664. 29.12 > Project Management > Project Management > /project-management-software/
665. 29.13 > Project Management > Project Planning > /project-planning-software/
666. 29.14 > Project Management > Project Portfolio Management > /project-portfolio-management-software/
667. 29.15 > Project Management > Project Tracking > /project-tracking-software/
668. 29.16 > Project Management > Requirements Management > /requirements-management-software/
669. 29.17 > Project Management > Resource Management > /resource-management-software/
670. 29.18 > Project Management > Scrum > /scrum-software/
671. 29.19 > Project Management > Spreadsheet > /spreadsheet-software/
672. 29.20 > Project Management > Task Management > /task-management-software/
673. 29.21 > Project Management > Time and Expense > /time-and-expense-software/
674. 29.22 > Project Management > Time Tracking > /time-tracking-software/
675. 29.23 > Project Management > Workflow Management > /workflow-management-software/
676. 30.0 > Real Estate > Commercial Real Estate > /commercial-real-estate-software/
677. 30.1 > Real Estate > HOA > /hoa-software/
678. 30.2 > Real Estate > Lease Management > /lease-management-software/
679. 30.3 > Real Estate > Real Estate Agency > /real-estate-agency-software/
680. 30.4 > Real Estate > Real Estate CMA > /real-estate-cma-software/
681. 30.5 > Real Estate > Real Estate CRM > /real-estate-crm-software/
682. 30.6 > Real Estate > Real Estate Property Management > /real-estate-property-management-software/
683. 30.7 > Real Estate > Real Estate Transaction Management > /real-estate-transaction-management-software/
684. 30.8 > Real Estate > Rental Property Management > /rental-property-management-software/
685. 30.9 > Real Estate > Virtual Tour > /virtual-tour-software/
686. 31.0 > Recreation > Camp Management > /camp-management-software/
687. 31.1 > Recreation > Campground Management > /campground-management-software/
688. 31.2 > Recreation > Club Management > /club-management-software/
689. 31.3 > Recreation > Dance Studio > /dance-studio-software/
690. 31.4 > Recreation > Driving School > /driving-school-software/
691. 31.5 > Recreation > Fitness > /fitness-software/
692. 31.6 > Recreation > Golf Course > /golf-course-software/
693. 31.7 > Recreation > Gymnastics > /gymnastics-software/
694. 31.8 > Recreation > Martial Arts > /martial-arts-software/
695. 31.9 > Recreation > Nutrition Analysis > /nutrition-analysis-software/
696. 31.10 > Recreation > Nutritionist > /nutritionist-software/
697. 31.11 > Recreation > Parks and Recreation > /parks-and-recreation-software/
698. 31.12 > Recreation > Personal Trainer > /personal-trainer-software/
699. 31.13 > Recreation > Pilates Studio > /pilates-studio-software/
700. 31.14 > Recreation > Pool Service > /pool-service-software/
701. 31.15 > Recreation > Sports League > /sports-league-software/
702. 31.16 > Recreation > Swim School > /swim-school-software/
703. 31.17 > Recreation > Yoga Studio > /yoga-studio-software/
704. 32.0 > Retail & Consumer > Android Kiosk > /android-kiosk-software/
705. 32.1 > Retail & Consumer > Apparel Management > /apparel-management-software/
706. 32.2 > Retail & Consumer > Art Gallery > /art-gallery-software/
707. 32.3 > Retail & Consumer > Auction > /auction-software/
708. 32.4 > Retail & Consumer > Auto Dealer > /auto-dealer-software/
709. 32.5 > Retail & Consumer > B2B Ecommerce Platform > /b2b-ecommerce-platform-software/
710. 32.6 > Retail & Consumer > Barbershop > /barbershop-software/
711. 32.7 > Retail & Consumer > Car Rental > /car-rental-software/
712. 32.8 > Retail & Consumer > Catalog Management > /catalog-management-software/
713. 32.9 > Retail & Consumer > Computer Repair Shop > /computer-repair-shop-software/
714. 32.10 > Retail & Consumer > Consignment > /consignment-software/
715. 32.11 > Retail & Consumer > Convenience Store > /convenience-store-software/
716. 32.12 > Retail & Consumer > Customer Advocacy > /customer-advocacy-software/
717. 32.13 > Retail & Consumer > Customer Loyalty > /customer-loyalty-software/
718. 32.14 > Retail & Consumer > Dry Cleaning > /dry-cleaning-software/
719. 32.15 > Retail & Consumer > eCommerce > /ecommerce-software/
720. 32.16 > Retail & Consumer > Equipment Rental > /equipment-rental-software/
721. 32.17 > Retail & Consumer > Fashion Design and Production > /fashion-design-and-production-software/
722. 32.18 > Retail & Consumer > Florist > /florist-software/
723. 32.19 > Retail & Consumer > Franchise Management > /franchise-management-software/
724. 32.20 > Retail & Consumer > Funeral Home > /funeral-home-software/
725. 32.21 > Retail & Consumer > Garden Center > /garden-center-software/
726. 32.22 > Retail & Consumer > Inventory Control > /inventory-control-software/
727. 32.23 > Retail & Consumer > iPad Kiosk > /ipad-kiosk-software/
728. 32.24 > Retail & Consumer > iPad POS > /ipad-pos-software/
729. 32.25 > Retail & Consumer > Jewelry Store Management > /jewelry-store-management-software/
730. 32.26 > Retail & Consumer > Kennel > /kennel-software/
731. 32.27 > Retail & Consumer > Kiosk > /kiosk-software/
732. 32.28 > Retail & Consumer > Locksmith > /locksmith-software/
733. 32.29 > Retail & Consumer > Lost and Found > /lost-and-found-software/
734. 32.30 > Retail & Consumer > Marketplace > /marketplace-software/
735. 32.31 > Retail & Consumer > Multi-Channel eCommerce > /multi-channel-ecommerce-software/
736. 32.32 > Retail & Consumer > Order Entry > /order-entry-software/
737. 32.33 > Retail & Consumer > Order Management > /order-management-software/
738. 32.34 > Retail & Consumer > Pawn Shop > /pawn-shop-software/
739. 32.35 > Retail & Consumer > Payment Processing > /payment-processing-software/
740. 32.36 > Retail & Consumer > Photography Studio > /photography-studio-software/
741. 32.37 > Retail & Consumer > Point of Sale > /point-of-sale-software/
742. 32.38 > Retail & Consumer > Rental > /rental-software/
743. 32.39 > Retail & Consumer > Retail Management Systems > /retail-management-systems-software/
744. 32.40 > Retail & Consumer > Retail POS System > /retail-pos-system-software/
745. 32.41 > Retail & Consumer > Sales Tax > /sales-tax-software/
746. 32.42 > Retail & Consumer > Salon > /salon-software/
747. 32.43 > Retail & Consumer > Self Storage > /self-storage-software/
748. 32.44 > Retail & Consumer > Shopping Cart > /shopping-cart-software/
749. 32.45 > Retail & Consumer > Small Business eCommerce > /small-business-ecommerce-software/
750. 32.46 > Retail & Consumer > Small Business Loyalty Programs > /small-business-loyalty-programs-software/
751. 32.47 > Retail & Consumer > Store Locator > /store-locator-software/
752. 32.48 > Retail & Consumer > Tattoo Studio > /tattoo-studio-software/
753. 32.49 > Retail & Consumer > Winery > /winery-software/
754. 33.0 > Sales > Channel Management > /channel-management-software/
755. 33.1 > Sales > Commission > /commission-software/
756. 33.2 > Sales > CPQ > /cpq-software/
757. 33.3 > Sales > Inside Sales > /inside-sales-software/
758. 33.4 > Sales > Lead Capture > /lead-capture-software/
759. 33.5 > Sales > Lead Management > /lead-management-software/
760. 33.6 > Sales > Lead Nurturing > /lead-nurturing-software/
761. 33.7 > Sales > MLM > /mlm-software/
762. 33.8 > Sales > Pricing Optimization > /pricing-optimization-software/
763. 33.9 > Sales > Proposal Management > /proposal-management-software/
764. 33.10 > Sales > Quoting > /quoting-software/
765. 33.11 > Sales > Referral > /referral-software/
766. 33.12 > Sales > Sales Coaching > /sales-coaching-software/
767. 33.13 > Sales > Sales Enablement > /sales-enablement-software/
768. 33.14 > Sales > Sales Force Automation > /sales-force-automation-software/
769. 33.15 > Sales > Sales Forecasting > /sales-forecasting-software/
770. 33.16 > Sales > Telemarketing > /telemarketing-software/
771. 33.17 > Sales > Warranty Management > /warranty-management-software/

## Python

```python
SUBCATEGORY_LIST = [
    "0. 0.0 > Accounting & Finance > Accounting > /accounting-software/",
    "1. 0.1 > Accounting & Finance > Accounting Practice Management > /accounting-practice-management-software/",
    "2. 0.2 > Accounting & Finance > Accounts Payable > /accounts-payable-software/",
    "3. 0.3 > Accounting & Finance > Accounts Receivable > /accounts-receivable-software/",
    "4. 0.4 > Accounting & Finance > Asset Tracking > /asset-tracking-software/",
    "5. 0.5 > Accounting & Finance > Auto Dealer Accounting > /auto-dealer-accounting-software/",
    "6. 0.6 > Accounting & Finance > Billing and Invoicing > /billing-and-invoicing-software/",
    "7. 0.7 > Accounting & Finance > Bookkeeper > /bookkeeper-software/",
    "8. 0.8 > Accounting & Finance > Budgeting > /budgeting-software/",
    "9. 0.9 > Accounting & Finance > Corporate Tax > /corporate-tax-software/",
    "10. 0.10 > Accounting & Finance > EAM > /eam-software/",
    "11. 0.11 > Accounting & Finance > Equity Management > /equity-management-software/",
    "12. 0.12 > Accounting & Finance > Expense Report > /expense-report-software/",
    "13. 0.13 > Accounting & Finance > Financial Management > /financial-management-software/",
    "14. 0.14 > Accounting & Finance > Financial Services > /financial-services-software/",
    "15. 0.15 > Accounting & Finance > Fixed Asset Management > /fixed-asset-management-software/",
    "16. 0.16 > Accounting & Finance > Lease Accounting > /lease-accounting-software/",
    "17. 0.17 > Accounting & Finance > Mobile Credit Card Processing > /mobile-credit-card-processing-software/",
    "18. 0.18 > Accounting & Finance > Nonprofit Accounting > /nonprofit-accounting-software/",
    "19. 0.19 > Accounting & Finance > Online Banking > /online-banking-software/",
    "20. 0.20 > Accounting & Finance > Purchasing > /purchasing-software/",
    "21. 0.21 > Accounting & Finance > Recurring Billing > /recurring-billing-software/",
    "22. 0.22 > Accounting & Finance > Revenue Management > /revenue-management-software/",
    "23. 0.23 > Accounting & Finance > Sourcing > /sourcing-software/",
    "24. 0.24 > Accounting & Finance > Spend management > /spend-management-software/",
    "25. 0.25 > Accounting & Finance > Tax Practice Management > /tax-practice-management-software/",
    "26. 0.26 > Accounting & Finance > Treasury > /treasury-software/",
    "27. 1.0 > Agriculture & Animal > Animal Shelter > /animal-shelter-software/",
    "28. 1.1 > Agriculture & Animal > Farm Management > /farm-management-software/",
    "29. 1.2 > Agriculture & Animal > Horse > /horse-software/",
    "30. 1.3 > Agriculture & Animal > Pet Grooming > /pet-grooming-software/",
    "31. 1.4 > Agriculture & Animal > Pet Sitting > /pet-sitting-software/",
    "32. 1.5 > Agriculture & Animal > Veterinary > /veterinary-software/",
    "33. 1.6 > Agriculture & Animal > Zoo > /zoo-software/",
    "34. 2.0 > Banking & Loans > AML > /aml-software/",
    "35. 2.1 > Banking & Loans > Banking Systems > /banking-systems-software/",
    "36. 2.2 > Banking & Loans > Commercial Loan > /commercial-loan-software/",
    "37. 2.3 > Banking & Loans > Currency Exchange > /currency-exchange-software/",
    "38. 2.4 > Banking & Loans > Debt Collection > /debt-collection-software/",
    "39. 2.5 > Banking & Loans > Financial CRM > /financial-crm-software/",
    "40. 2.6 > Banking & Loans > Financial Fraud Detection > /financial-fraud-detection-software/",
    "41. 2.7 > Banking & Loans > Financial Risk Management > /financial-risk-management-software/",
    "42. 2.8 > Banking & Loans > Hedge Fund > /hedge-fund-software/",
    "43. 2.9 > Banking & Loans > Investment Management > /investment-management-software/",
    "44. 2.10 > Banking & Loans > Loan Origination > /loan-origination-software/",
    "45. 2.11 > Banking & Loans > Loan Servicing > /loan-servicing-software/",
    "46. 2.12 > Banking & Loans > Mobile Banking > /mobile-banking-software/",
    "47. 2.13 > Banking & Loans > Mortgage and Loans > /mortgage-and-loans-software/",
    "48. 2.14 > Banking & Loans > Stock Portfolio Management > /stock-portfolio-management-software/",
    "49. 3.0 > Business Operations > Bankruptcy > /bankruptcy-software/",
    "50. 3.1 > Business Operations > Board Management > /board-management-software/",
    "51. 3.2 > Business Operations > Business Intelligence > /business-intelligence-software/",
    "52. 3.3 > Business Operations > Business Management > /business-management-software/",
    "53. 3.4 > Business Operations > Business Performance Management > /business-performance-management-software/",
    "54. 3.5 > Business Operations > Business Plan > /business-plan-software/",
    "55. 3.6 > Business Operations > Business Process Management > /business-process-management-software/",
    "56. 3.7 > Business Operations > Company Secretarial > /company-secretarial-software/",
    "57. 3.8 > Business Operations > Competitive Intelligence > /competitive-intelligence-software/",
    "58. 3.9 > Business Operations > Contract Management > /contract-management-software/",
    "59. 3.10 > Business Operations > Dashboard > /dashboard-software/",
    "60. 3.11 > Business Operations > Decision Support > /decision-support-software/",
    "61. 3.12 > Business Operations > Enterprise Resource Planning > /enterprise-resource-planning-software/",
    "62. 3.13 > Business Operations > Financial Reporting > /financial-reporting-software/",
    "63. 3.14 > Business Operations > Flowchart > /flowchart-software/",
    "64. 3.15 > Business Operations > Location Intelligence > /location-intelligence-software/",
    "65. 3.16 > Business Operations > OKR > /okr-software/",
    "66. 3.17 > Business Operations > Policy Management > /policy-management-software/",
    "67. 3.18 > Business Operations > Procurement > /procurement-software/",
    "68. 3.19 > Business Operations > Productivity > /productivity-software/",
    "69. 3.20 > Business Operations > Remote Work > /remote-work-software/",
    "70. 3.21 > Business Operations > Reporting > /reporting-software/",
    "71. 3.22 > Business Operations > RFP > /rfp-software/",
    "72. 3.23 > Business Operations > Statistical Analysis > /statistical-analysis-software/",
    "73. 3.24 > Business Operations > Strategic Planning > /strategic-planning-software/",
    "74. 4.0 > Communications & Media > Auto Dialer > /auto-dialer-software/",
    "75. 4.1 > Communications & Media > Billing and Provisioning > /billing-and-provisioning-software/",
    "76. 4.2 > Communications & Media > Business Phone Systems > /business-phone-systems-software/",
    "77. 4.3 > Communications & Media > Call Accounting > /call-accounting-software/",
    "78. 4.4 > Communications & Media > Call Recording > /call-recording-software/",
    "79. 4.5 > Communications & Media > Call Tracking > /call-tracking-software/",
    "80. 4.6 > Communications & Media > Cloud Communication Platform > /cloud-communication-platform-software/",
    "81. 4.7 > Communications & Media > Cloud PBX > /cloud-pbx-software/",
    "82. 4.8 > Communications & Media > Collaboration > /collaboration-software/",
    "83. 4.9 > Communications & Media > Community > /community-software/",
    "84. 4.10 > Communications & Media > Digital Workplace > /digital-workplace-software/",
    "85. 4.11 > Communications & Media > Fax Server > /fax-server-software/",
    "86. 4.12 > Communications & Media > Internal Communications > /internal-communications-software/",
    "87. 4.13 > Communications & Media > IVR > /ivr-software/",
    "88. 4.14 > Communications & Media > Mobile Device Management > /mobile-device-management-software/",
    "89. 4.15 > Communications & Media > Predictive Dialer > /predictive-dialer-software/",
    "90. 4.16 > Communications & Media > Presentation > /presentation-software/",
    "91. 4.17 > Communications & Media > Print Estimating > /print-estimating-software/",
    "92. 4.18 > Communications & Media > Publishing and Subscriptions > /publishing-and-subscriptions-software/",
    "93. 4.19 > Communications & Media > Screen Recording > /screen-recording-software/",
    "94. 4.20 > Communications & Media > Screen Sharing > /screen-sharing-software/",
    "95. 4.21 > Communications & Media > Softphone  > /softphone-software/",
    "96. 4.22 > Communications & Media > Speech Recognition > /speech-recognition-software/",
    "97. 4.23 > Communications & Media > Subscription Management > /subscription-management-software/",
    "98. 4.24 > Communications & Media > Team Communication > /team-communication-software/",
    "99. 4.25 > Communications & Media > Telecom Expense Management > /telecom-expense-management-software/",
    "100. 4.26 > Communications & Media > Telephony > /telephony-software/",
    "101. 4.27 > Communications & Media > Transcription > /transcription-software/",
    "102. 4.28 > Communications & Media > Translation Management > /translation-management-software/",
    "103. 4.29 > Communications & Media > Unified Communications > /unified-communications-software/",
    "104. 4.30 > Communications & Media > Video Conferencing  > /video-conferencing-software/",
    "105. 4.31 > Communications & Media > Video Editing > /video-editing-software/",
    "106. 4.32 > Communications & Media > Video Making > /video-making-software/",
    "107. 4.33 > Communications & Media > Video Management > /video-management-software/",
    "108. 4.34 > Communications & Media > VoIP > /voip-software/",
    "109. 4.35 > Communications & Media > Web Conferencing > /web-conferencing-software/",
    "110. 4.36 > Communications & Media > Webinar > /webinar-software/",
    "111. 4.37 > Communications & Media > Wireless Expense Management > /wireless-expense-management-software/",
    "112. 5.0 > Compliance & Risk Management > Accreditation Management > /accreditation-management-software/",
    "113. 5.1 > Compliance & Risk Management > Audit > /audit-software/",
    "114. 5.2 > Compliance & Risk Management > Compliance > /compliance-software/",
    "115. 5.3 > Compliance & Risk Management > Corrective and Preventive Action (CAPA) > /corrective-and-preventive-action-software/",
    "116. 5.4 > Compliance & Risk Management > GDPR Compliance > /gdpr-compliance-software/",
    "117. 5.5 > Compliance & Risk Management > GRC > /grc-software/",
    "118. 5.6 > Compliance & Risk Management > Integrated Risk Management > /integrated-risk-management-software/",
    "119. 5.7 > Compliance & Risk Management > IT Asset Management > /it-asset-management-software/",
    "120. 5.8 > Compliance & Risk Management > License Management > /license-management-software/",
    "121. 5.9 > Compliance & Risk Management > PCI Compliance > /pci-compliance-software/",
    "122. 5.10 > Compliance & Risk Management > Risk Management > /risk-management-software/",
    "123. 6.0 > Construction > 3D Architecture > /3d-architecture-software/",
    "124. 6.1 > Construction > 3D CAD > /3d-cad-software/",
    "125. 6.2 > Construction > Architectural CAD > /architectural-cad-software/",
    "126. 6.3 > Construction > Architecture > /architecture-software/",
    "127. 6.4 > Construction > Construction Accounting > /construction-accounting-software/",
    "128. 6.5 > Construction > Construction Bid Management > /construction-bid-management-software/",
    "129. 6.6 > Construction > Construction CRM > /construction-crm-software/",
    "130. 6.7 > Construction > Construction Estimating > /construction-estimating-software/",
    "131. 6.8 > Construction > Construction Management > /construction-management-software/",
    "132. 6.9 > Construction > Construction Scheduling > /construction-scheduling-software/",
    "133. 6.10 > Construction > Contractor Management > /contractor-management-software/",
    "134. 6.11 > Construction > Home Builder > /home-builder-software/",
    "135. 6.12 > Construction > Punch List > /punch-list-software/",
    "136. 6.13 > Construction > Remodeling Estimating > /remodeling-estimating-software/",
    "137. 6.14 > Construction > Residential Construction Estimating > /residential-construction-estimating-software/",
    "138. 6.15 > Construction > Takeoff > /takeoff-software/",
    "139. 7.0 > Content & Document > Archiving > /archiving-software/",
    "140. 7.1 > Content & Document > Blog > /blog-software/",
    "141. 7.2 > Content & Document > Content Management > /content-management-software/",
    "142. 7.3 > Content & Document > Digital Asset Management > /digital-asset-management-software/",
    "143. 7.4 > Content & Document > Digital Signage > /digital-signage-software/",
    "144. 7.5 > Content & Document > Digital Signature > /digital-signature-software/",
    "145. 7.6 > Content & Document > Directory > /directory-software/",
    "146. 7.7 > Content & Document > Document Control > /document-control-software/",
    "147. 7.8 > Content & Document > Document Generation > /document-generation-software/",
    "148. 7.9 > Content & Document > Document Management > /document-management-software/",
    "149. 7.10 > Content & Document > Document Version Control > /document-version-control-software/",
    "150. 7.11 > Content & Document > Enterprise Content Management > /enterprise-content-management-software/",
    "151. 7.12 > Content & Document > Enterprise Search > /enterprise-search-software/",
    "152. 7.13 > Content & Document > File Sharing > /file-sharing-software/",
    "153. 7.14 > Content & Document > File Sync > /file-sync-software/",
    "154. 7.15 > Content & Document > Forms Automation > /forms-automation-software/",
    "155. 7.16 > Content & Document > Mobile Content Management > /mobile-content-management-system-software/",
    "156. 7.17 > Content & Document > OCR > /ocr-software/",
    "157. 7.18 > Content & Document > PDF > /pdf-software/",
    "158. 7.19 > Content & Document > Proofreading > /proofreading-software/",
    "159. 7.20 > Content & Document > SEO > /seo-software/",
    "160. 7.21 > Content & Document > Visual Search > /visual-search-software/",
    "161. 7.22 > Content & Document > Waiver > /waiver-software/",
    "162. 7.23 > Content & Document > Web to Print > /web-to-print-software/",
    "163. 8.0 > Customer Management > Call Center > /call-center-software/",
    "164. 8.1 > Customer Management > Complaint Management > /complaint-management-software/",
    "165. 8.2 > Customer Management > Contact Management > /contact-management-software/",
    "166. 8.3 > Customer Management > Customer Communications Management > /customer-communications-management-software/",
    "167. 8.4 > Customer Management > Customer Engagement > /customer-engagement-software/",
    "168. 8.5 > Customer Management > Customer Experience > /customer-experience-software/",
    "169. 8.6 > Customer Management > Customer Reference Management > /customer-reference-management-software/",
    "170. 8.7 > Customer Management > Customer Relationship Management > /customer-relationship-management-software/",
    "171. 8.8 > Customer Management > Customer Satisfaction > /customer-satisfaction-software/",
    "172. 8.9 > Customer Management > Customer Service > /customer-service-software/",
    "173. 8.10 > Customer Management > Customer Success > /customer-success-software/",
    "174. 8.11 > Customer Management > Digital Adoption Platform > /digital-adoption-platform-software/",
    "175. 8.12 > Customer Management > Help Desk > /help-desk-software/",
    "176. 8.13 > Customer Management > Incident Management > /incident-management-software/",
    "177. 8.14 > Customer Management > Knowledge Management > /knowledge-management-software/",
    "178. 8.15 > Customer Management > Live Chat > /live-chat-software/",
    "179. 8.16 > Customer Management > Mac CRM > /mac-crm-software/",
    "180. 8.17 > Customer Management > Nonprofit CRM > /nonprofit-crm-software/",
    "181. 8.18 > Customer Management > Online CRM > /online-crm-software/",
    "182. 8.19 > Customer Management > Service Desk > /service-desk-software/",
    "183. 8.20 > Customer Management > Small Business CRM > /small-business-crm-software/",
    "184. 8.21 > Customer Management > Social CRM Tools > /social-crm-tools-software/",
    "185. 9.0 > Data Management > Big Data > /big-data-software/",
    "186. 9.1 > Data Management > Business Continuity > /business-continuity-software/",
    "187. 9.2 > Data Management > Data Analysis > /data-analysis-software/",
    "188. 9.3 > Data Management > Data Center Management > /data-center-management-software/",
    "189. 9.4 > Data Management > Data Discovery > /data-discovery-software/",
    "190. 9.5 > Data Management > Data Entry > /data-entry-software/",
    "191. 9.6 > Data Management > Data Extraction > /data-extraction-software/",
    "192. 9.7 > Data Management > Data Governance > /data-governance-software/",
    "193. 9.8 > Data Management > Data Management > /data-management-software/",
    "194. 9.9 > Data Management > Data Mining > /data-mining-software/",
    "195. 9.10 > Data Management > Data Quality > /data-quality-software/",
    "196. 9.11 > Data Management > Data Visualization > /data-visualization-software/",
    "197. 9.12 > Data Management > Data Warehouse > /data-warehouse-software/",
    "198. 9.13 > Data Management > Database Management > /database-management-software/",
    "199. 9.14 > Data Management > Database Monitoring > /database-monitoring-software/",
    "200. 9.15 > Data Management > EDI > /edi-software/",
    "201. 9.16 > Data Management > Electronic Data Capture > /electronic-data-capture-software/",
    "202. 9.17 > Data Management > Email Archiving  > /email-archiving-software/",
    "203. 9.18 > Data Management > Email Management > /email-management-software/",
    "204. 9.19 > Data Management > Email Signature > /email-signature-software/",
    "205. 9.20 > Data Management > Embedded Analytics > /embedded-analytics-software/",
    "206. 9.21 > Data Management > ETL > /etl-software/",
    "207. 9.22 > Data Management > Master Data Management > /master-data-management-software/",
    "208. 9.23 > Data Management > Mobile Analytics > /mobile-analytics-software/",
    "209. 9.24 > Data Management > Portal > /portal-software/",
    "210. 9.25 > Data Management > Predictive Analytics > /predictive-analytics-software/",
    "211. 9.26 > Data Management > Qualitative Data Analysis > /qualitative-data-analysis-software/",
    "212. 9.27 > Data Management > RDBMS > /rdbms-software/",
    "213. 9.28 > Data Management > Text Mining > /text-mining-software/",
    "214. 9.29 > Data Management > Virtual Data Room > /virtual-data-room-software/",
    "215. 9.30 > Data Management > Web Analytics > /web-analytics-software/",
    "216. 10.0 > Education & eLearning > Admissions > /admissions-software/",
    "217. 10.1 > Education & eLearning > Alumni Management > /alumni-management-software/",
    "218. 10.2 > Education & eLearning > Assessment > /assessment-software/",
    "219. 10.3 > Education & eLearning > Child Care > /child-care-software/",
    "220. 10.4 > Education & eLearning > Class Registration > /class-registration-software/",
    "221. 10.5 > Education & eLearning > Classroom Management > /classroom-management-software/",
    "222. 10.6 > Education & eLearning > Course Authoring > /course-authoring-software/",
    "223. 10.7 > Education & eLearning > eLearning Authoring Tools > /elearning-authoring-tools-software/",
    "224. 10.8 > Education & eLearning > Exam > /exam-software/",
    "225. 10.9 > Education & eLearning > Gradebook > /gradebook-software/",
    "226. 10.10 > Education & eLearning > Higher Education > /higher-education-software/",
    "227. 10.11 > Education & eLearning > K-12 > /k-12-software/",
    "228. 10.12 > Education & eLearning > Learning Experience Platform (LEP) > /learning-experience-platform-software/",
    "229. 10.13 > Education & eLearning > Learning Management System > /learning-management-system-software/",
    "230. 10.14 > Education & eLearning > Library Automation > /library-automation-software/",
    "231. 10.15 > Education & eLearning > Microlearning > /microlearning-software/",
    "232. 10.16 > Education & eLearning > Mobile Learning > /mobile-learning-software/",
    "233. 10.17 > Education & eLearning > Music School > /music-school-software/",
    "234. 10.18 > Education & eLearning > Scholarship Management > /scholarship-management-software/",
    "235. 10.19 > Education & eLearning > School Accounting > /school-accounting-software/",
    "236. 10.20 > Education & eLearning > School Administration > /school-administration-software/",
    "237. 10.21 > Education & eLearning > Student Engagement Platform > /student-engagement-platform-software/",
    "238. 10.22 > Education & eLearning > Student Information System > /student-information-system-software/",
    "239. 10.23 > Education & eLearning > Training > /training-software/",
    "240. 10.24 > Education & eLearning > Tutoring > /tutoring-software/",
    "241. 10.25 > Education & eLearning > Virtual Classroom > /virtual-classroom-software/",
    "242. 10.26 > Education & eLearning > Whiteboard > /whiteboard-software/",
    "243. 11.0 > Energy & Environment > EHS Management > /ehs-management-software/",
    "244. 11.1 > Energy & Environment > Emissions Management > /emissions-management-software/",
    "245. 11.2 > Energy & Environment > Energy Management > /energy-management-software/",
    "246. 11.3 > Energy & Environment > Environmental > /environmental-software/",
    "247. 11.4 > Energy & Environment > Forestry > /forestry-software/",
    "248. 11.5 > Energy & Environment > GIS > /gis-software/",
    "249. 11.6 > Energy & Environment > Land Management > /land-management-software/",
    "250. 11.7 > Energy & Environment > Mining > /mining-software/",
    "251. 11.8 > Energy & Environment > Oil and Gas > /oil-and-gas-software/",
    "252. 11.9 > Energy & Environment > Safety Management > /safety-management-software/",
    "253. 11.10 > Energy & Environment > Sustainability > /sustainability-software/",
    "254. 11.11 > Energy & Environment > Utility Billing > /utility-billing-software/",
    "255. 11.12 > Energy & Environment > Utility Management Systems > /utility-management-systems-software/",
    "256. 12.0 > Event > Audience Response > /audience-response-software/",
    "257. 12.1 > Event > Conference > /conference-software/",
    "258. 12.2 > Event > Event Booking > /event-booking-software/",
    "259. 12.3 > Event > Event Check In > /event-check-in-software/",
    "260. 12.4 > Event > Event Management > /event-management-software/",
    "261. 12.5 > Event > Event Marketing > /event-marketing-software/",
    "262. 12.6 > Event > Festival Management > /festival-management-software/",
    "263. 12.7 > Event > Live Streaming > /live-streaming-software/",
    "264. 12.8 > Event > Meeting > /meeting-software/",
    "265. 12.9 > Event > Mobile Event Apps > /mobile-event-apps-software/",
    "266. 12.10 > Event > Registration > /registration-software/",
    "267. 12.11 > Event > Ticketing > /ticketing-software/",
    "268. 12.12 > Event > Venue Management > /venue-management-software/",
    "269. 12.13 > Event > Virtual Event > /virtual-event-software/",
    "270. 13.0 > Facility > Appointment Reminder > /appointment-reminder-software/",
    "271. 13.1 > Facility > Appointment Scheduling > /appointment-scheduling-software/",
    "272. 13.2 > Facility > Facility Management > /facility-management-software/",
    "273. 13.3 > Facility > IWMS > /iwms-software/",
    "274. 13.4 > Facility > Key Management > /key-management-software/",
    "275. 13.5 > Facility > Mailroom Management > /mailroom-management-software/",
    "276. 13.6 > Facility > Meeting Room Booking > /meeting-room-booking-system-software/",
    "277. 13.7 > Facility > Physical Security > /physical-security-software/",
    "278. 13.8 > Facility > Scheduling > /scheduling-software/",
    "279. 13.9 > Facility > Space Management > /space-management-software/",
    "280. 13.10 > Facility > Visitor Management > /visitor-management-software/",
    "281. 13.11 > Facility > Waitlist > /waitlist-software/",
    "282. 14.0 > Field Service > Arborist > /arborist-software/",
    "283. 14.1 > Field Service > Carpet Cleaning > /carpet-cleaning-software/",
    "284. 14.2 > Field Service > Electrical Contractor > /electrical-contractor-software/",
    "285. 14.3 > Field Service > Electrical Estimating > /electrical-estimating-software/",
    "286. 14.4 > Field Service > Field Service Management > /field-service-management-software/",
    "287. 14.5 > Field Service > Garage Door > /garage-door-software/",
    "288. 14.6 > Field Service > Handyman > /handyman-software/",
    "289. 14.7 > Field Service > Home Inspection > /home-inspection-software/",
    "290. 14.8 > Field Service > HVAC > /hvac-software/",
    "291. 14.9 > Field Service > HVAC Estimating > /hvac-estimating-software/",
    "292. 14.10 > Field Service > Inspection > /inspection-software/",
    "293. 14.11 > Field Service > IT Service > /it-service-software/",
    "294. 14.12 > Field Service > Janitorial > /janitorial-software/",
    "295. 14.13 > Field Service > Landscape > /landscape-software/",
    "296. 14.14 > Field Service > Lawn Care > /lawn-care-software/",
    "297. 14.15 > Field Service > Maid Service > /maid-service-software/",
    "298. 14.16 > Field Service > Pest Control > /pest-control-software/",
    "299. 14.17 > Field Service > Plumbing > /plumbing-software/",
    "300. 14.18 > Field Service > Plumbing Estimating > /plumbing-estimating-software/",
    "301. 14.19 > Field Service > Recycling > /recycling-software/",
    "302. 14.20 > Field Service > Roofing > /roofing-software/",
    "303. 14.21 > Field Service > Security System Installer > /security-system-installer-software/",
    "304. 14.22 > Field Service > Service Dispatch > /service-dispatch-software/",
    "305. 14.23 > Field Service > Waste Management > /waste-management-software/",
    "306. 14.24 > Field Service > Work Order > /work-order-software/",
    "307. 15.0 > Food Service > Bakery > /bakery-software/",
    "308. 15.1 > Food Service > Bar POS > /bar-pos-software/",
    "309. 15.2 > Food Service > Brewery > /brewery-software/",
    "310. 15.3 > Food Service > Catering > /catering-software/",
    "311. 15.4 > Food Service > Food Costing > /food-costing-software/",
    "312. 15.5 > Food Service > Food Delivery > /food-delivery-software/",
    "313. 15.6 > Food Service > Food Service Distribution > /food-service-distribution-software/",
    "314. 15.7 > Food Service > Food Service Management > /food-service-management-software/",
    "315. 15.8 > Food Service > Food Traceability > /food-traceability-software/",
    "316. 15.9 > Food Service > Restaurant Management > /restaurant-management-software/",
    "317. 15.10 > Food Service > Restaurant POS > /restaurant-pos-software/",
    "318. 16.0 > Healthcare & Medical > Applied Behavior Analysis > /applied-behavior-analysis-software/",
    "319. 16.1 > Healthcare & Medical > Assisted Living > /assisted-living-software/",
    "320. 16.2 > Healthcare & Medical > Chiropractic > /chiropractic-software/",
    "321. 16.3 > Healthcare & Medical > Clinical Trial Management > /clinical-trial-management-software/",
    "322. 16.4 > Healthcare & Medical > Credentialing > /credentialing-software/",
    "323. 16.5 > Healthcare & Medical > Dental > /dental-software/",
    "324. 16.6 > Healthcare & Medical > Dental Charting > /dental-charting-software/",
    "325. 16.7 > Healthcare & Medical > Dental Imaging > /dental-imaging-software/",
    "326. 16.8 > Healthcare & Medical > Dermatology > /dermatology-software/",
    "327. 16.9 > Healthcare & Medical > e-Prescribing > /eprescribing-software/",
    "328. 16.10 > Healthcare & Medical > Electronic Medical Records > /electronic-medical-records-software/",
    "329. 16.11 > Healthcare & Medical > EMS > /ems-software/",
    "330. 16.12 > Healthcare & Medical > Healthcare CRM > /healthcare-crm-software/",
    "331. 16.13 > Healthcare & Medical > HIPAA Compliance > /hipaa-compliance-software/",
    "332. 16.14 > Healthcare & Medical > Home Care > /home-care-software/",
    "333. 16.15 > Healthcare & Medical > Home Health Care > /home-health-care-software/",
    "334. 16.16 > Healthcare & Medical > Hospice > /hospice-software/",
    "335. 16.17 > Healthcare & Medical > Hospital Management > /hospital-management-software/",
    "336. 16.18 > Healthcare & Medical > Laboratory Information Management System > /laboratory-information-management-system-software/",
    "337. 16.19 > Healthcare & Medical > Long Term Care > /long-term-care-software/",
    "338. 16.20 > Healthcare & Medical > Massage Therapy > /massage-therapy-software/",
    "339. 16.21 > Healthcare & Medical > Medical Billing > /medical-billing-software/",
    "340. 16.22 > Healthcare & Medical > Medical Imaging > /medical-imaging-software/",
    "341. 16.23 > Healthcare & Medical > Medical Inventory > /medical-inventory-software/",
    "342. 16.24 > Healthcare & Medical > Medical Lab > /medical-lab-software/",
    "343. 16.25 > Healthcare & Medical > Medical Practice Management > /medical-practice-management-software/",
    "344. 16.26 > Healthcare & Medical > Medical Scheduling > /medical-scheduling-software/",
    "345. 16.27 > Healthcare & Medical > Medical Spa > /medical-spa-software/",
    "346. 16.28 > Healthcare & Medical > Medical Transcription > /medical-transcription-software/",
    "347. 16.29 > Healthcare & Medical > Mental Health > /mental-health-software/",
    "348. 16.30 > Healthcare & Medical > Nurse Scheduling > /nurse-scheduling-software/",
    "349. 16.31 > Healthcare & Medical > Nursing Home > /nursing-home-software/",
    "350. 16.32 > Healthcare & Medical > Occupational Therapy > /occupational-therapy-software/",
    "351. 16.33 > Healthcare & Medical > Optometry > /optometry-software/",
    "352. 16.34 > Healthcare & Medical > PACS > /pacs-software/",
    "353. 16.35 > Healthcare & Medical > Patient Case Management > /patient-case-management-software/",
    "354. 16.36 > Healthcare & Medical > Patient Engagement > /patient-engagement-software/",
    "355. 16.37 > Healthcare & Medical > Patient Management > /patient-management-software/",
    "356. 16.38 > Healthcare & Medical > Patient Portal > /patient-portal-software/",
    "357. 16.39 > Healthcare & Medical > Pediatric > /pediatric-software/",
    "358. 16.40 > Healthcare & Medical > Pharmacy > /pharmacy-software/",
    "359. 16.41 > Healthcare & Medical > Physical Therapy > /physical-therapy-software/",
    "360. 16.42 > Healthcare & Medical > Plastic Surgery > /plastic-surgery-software/",
    "361. 16.43 > Healthcare & Medical > Podiatry > /podiatry-software/",
    "362. 16.44 > Healthcare & Medical > Radiology > /radiology-software/",
    "363. 16.45 > Healthcare & Medical > Remote Patient Monitoring > /remote-patient-monitoring-software/",
    "364. 16.46 > Healthcare & Medical > Speech Therapy > /speech-therapy-software/",
    "365. 16.47 > Healthcare & Medical > Telemedicine > /telemedicine-software/",
    "366. 17.0 > Hospitality & Travel > Airline Reservation System > /airline-reservation-system-software/",
    "367. 17.1 > Hospitality & Travel > Hospitality Property Management > /hospitality-property-management-software/",
    "368. 17.2 > Hospitality & Travel > Hostel Management > /hostel-management-software/",
    "369. 17.3 > Hospitality & Travel > Hotel Channel Management > /hotel-channel-management-software/",
    "370. 17.4 > Hospitality & Travel > Reservations > /reservations-software/",
    "371. 17.5 > Hospitality & Travel > Spa > /spa-software/",
    "372. 17.6 > Hospitality & Travel > Timeshare > /timeshare-software/",
    "373. 17.7 > Hospitality & Travel > Tour Operator > /tour-operator-software/",
    "374. 17.8 > Hospitality & Travel > Travel Agency > /travel-agency-software/",
    "375. 17.9 > Hospitality & Travel > Travel Management > /travel-management-software/",
    "376. 17.10 > Hospitality & Travel > Vacation Rental > /vacation-rental-software/",
    "377. 18.0 > HR & Talent > 360 Degree Feedback > /360-degree-feedback-software/",
    "378. 18.1 > HR & Talent > Applicant Tracking > /applicant-tracking-software/",
    "379. 18.2 > HR & Talent > Attendance Tracking > /attendance-tracking-software/",
    "380. 18.3 > HR & Talent > Background Check > /background-check-software/",
    "381. 18.4 > HR & Talent > Benefits Administration > /benefits-administration-software/",
    "382. 18.5 > HR & Talent > Business Card > /business-card-software/",
    "383. 18.6 > HR & Talent > Coaching > /coaching-software/",
    "384. 18.7 > HR & Talent > Compensation Management > /compensation-management-software/",
    "385. 18.8 > HR & Talent > Corporate Wellness > /corporate-wellness-software/",
    "386. 18.9 > HR & Talent > Employee Communication Tools > /employee-communication-tools-software/",
    "387. 18.10 > HR & Talent > Employee Engagement > /employee-engagement-software/",
    "388. 18.11 > HR & Talent > Employee Monitoring > /employee-monitoring-software/",
    "389. 18.12 > HR & Talent > Employee Recognition > /employee-recognition-software/",
    "390. 18.13 > HR & Talent > Employee Scheduling > /employee-scheduling-software/",
    "391. 18.14 > HR & Talent > HR Analytics > /hr-analytics-software/",
    "392. 18.15 > HR & Talent > Human Resource > /human-resource-software/",
    "393. 18.16 > HR & Talent > Job Board > /job-board-software/",
    "394. 18.17 > HR & Talent > Job Evaluation > /job-evaluation-software/",
    "395. 18.18 > HR & Talent > Leave Management System > /leave-management-system-software/",
    "396. 18.19 > HR & Talent > Mentoring > /mentoring-software/",
    "397. 18.20 > HR & Talent > Onboarding > /onboarding-software/",
    "398. 18.21 > HR & Talent > Org Chart > /org-chart-software/",
    "399. 18.22 > HR & Talent > Payroll > /payroll-software/",
    "400. 18.23 > HR & Talent > Performance Appraisal > /performance-appraisal-software/",
    "401. 18.24 > HR & Talent > Pre-employment Testing > /pre-employment-testing-software/",
    "402. 18.25 > HR & Talent > Recruiting > /recruiting-software/",
    "403. 18.26 > HR & Talent > Recruiting Agency > /recruiting-agency-software/",
    "404. 18.27 > HR & Talent > Reference Check > /reference-check-software/",
    "405. 18.28 > HR & Talent > Relocation > /relocation-software/",
    "406. 18.29 > HR & Talent > Staffing Agency > /staffing-agency-software/",
    "407. 18.30 > HR & Talent > Succession Planning > /succession-planning-software/",
    "408. 18.31 > HR & Talent > Talent Management > /talent-management-software/",
    "409. 18.32 > HR & Talent > Time Clock > /time-clock-software/",
    "410. 18.33 > HR & Talent > Video Interviewing > /video-interviewing-software/",
    "411. 18.34 > HR & Talent > Workforce Management > /workforce-management-software/",
    "412. 19.0 > Insurance > Claims Processing > /claims-processing-software/",
    "413. 19.1 > Insurance > Commercial Insurance > /commercial-insurance-software/",
    "414. 19.2 > Insurance > Insurance Agency > /insurance-agency-software/",
    "415. 19.3 > Insurance > Insurance Policy > /insurance-policy-software/",
    "416. 19.4 > Insurance > Insurance Rating > /insurance-rating-software/",
    "417. 19.5 > Insurance > P&C Insurance > /p-c-insurance-software/",
    "418. 20.0 > IT & Development > API Management > /api-management-software/",
    "419. 20.1 > IT & Development > App Building > /app-building-software/",
    "420. 20.2 > IT & Development > App Design > /app-design-software/",
    "421. 20.3 > IT & Development > Application Development > /application-development-software/",
    "422. 20.4 > IT & Development > Application Lifecycle Management > /application-lifecycle-management-software/",
    "423. 20.5 > IT & Development > Application Performance Management > /application-performance-management-software/",
    "424. 20.6 > IT & Development > Artificial Intelligence > /artificial-intelligence-software/",
    "425. 20.7 > IT & Development > Augmented Reality > /augmented-reality-software/",
    "426. 20.8 > IT & Development > Automated Testing > /automated-testing-software/",
    "427. 20.9 > IT & Development > Backup > /backup-software/",
    "428. 20.10 > IT & Development > Change Management > /change-management-software/",
    "429. 20.11 > IT & Development > Cloud Management > /cloud-management-software/",
    "430. 20.12 > IT & Development > Cloud Storage > /cloud-storage-software/",
    "431. 20.13 > IT & Development > CMDB > /cmdb-software/",
    "432. 20.14 > IT & Development > Continuous Integration > /continuous-integration-software/",
    "433. 20.15 > IT & Development > Conversational AI > /conversational-ai-platform-software/",
    "434. 20.16 > IT & Development > Data Loss Prevention > /data-loss-prevention-software/",
    "435. 20.17 > IT & Development > Deep Learning > /deep-learning-software/",
    "436. 20.18 > IT & Development > DevOps > /devops-software/",
    "437. 20.19 > IT & Development > Disk Imaging > /disk-imaging-software/",
    "438. 20.20 > IT & Development > Enterprise Architecture > /enterprise-architecture-software/",
    "439. 20.21 > IT & Development > Game Development > /game-development-software/",
    "440. 20.22 > IT & Development > Identity Management > /identity-management-software/",
    "441. 20.23 > IT & Development > Infrastructure as a Service (IaaS) > /infrastructure-as-a-service-solutions-software/",
    "442. 20.24 > IT & Development > Integration > /integration-software/",
    "443. 20.25 > IT & Development > Intranet > /intranet-software/",
    "444. 20.26 > IT & Development > IoT > /iot-software/",
    "445. 20.27 > IT & Development > IT Management > /it-management-software/",
    "446. 20.28 > IT & Development > ITSM > /itsm-software/",
    "447. 20.29 > IT & Development > Java CMS > /java-cms-software/",
    "448. 20.30 > IT & Development > Load Balancing > /load-balancing-software/",
    "449. 20.31 > IT & Development > Log Management > /log-management-software/",
    "450. 20.32 > IT & Development > Logbook > /logbook-software/",
    "451. 20.33 > IT & Development > Low Code Development Platform > /low-code-development-platform-software/",
    "452. 20.34 > IT & Development > Machine Learning > /machine-learning-software/",
    "453. 20.35 > IT & Development > Mobility > /mobility-software/",
    "454. 20.36 > IT & Development > MSP > /msp-software/",
    "455. 20.37 > IT & Development > Network Mapping > /network-mapping-software/",
    "456. 20.38 > IT & Development > Network Monitoring > /network-monitoring-software/",
    "457. 20.39 > IT & Development > Network Troubleshooting > /network-troubleshooting-software/",
    "458. 20.40 > IT & Development > Patch Management > /patch-management-software/",
    "459. 20.41 > IT & Development > Performance Testing > /performance-testing-software/",
    "460. 20.42 > IT & Development > Remote Desktop > /remote-desktop-software/",
    "461. 20.43 > IT & Development > Remote Monitoring and Management > /remote-monitoring-and-management-software/",
    "462. 20.44 > IT & Development > Remote Support > /remote-support-software/",
    "463. 20.45 > IT & Development > Robotic Process Automation (RPA) > /robotic-process-automation-software/",
    "464. 20.46 > IT & Development > SaaS Management > /saas-management-software/",
    "465. 20.47 > IT & Development > Server Backup > /server-backup-software/",
    "466. 20.48 > IT & Development > Server Management > /server-management-software/",
    "467. 20.49 > IT & Development > Source Code Management > /source-code-management-software/",
    "468. 20.50 > IT & Development > VDI > /vdi-software/",
    "469. 20.51 > IT & Development > Virtual Machine > /virtual-machine-software/",
    "470. 20.52 > IT & Development > Virtualization > /virtualization-software/",
    "471. 20.53 > IT & Development > VPN > /vpn-software/",
    "472. 20.54 > IT & Development > VR > /vr-software/",
    "473. 20.55 > IT & Development > Website Builder > /website-builder-software/",
    "474. 20.56 > IT & Development > Website Monitoring > /website-monitoring-software/",
    "475. 20.57 > IT & Development > Website Optimization Tools > /website-optimization-tools-software/",
    "476. 21.0 > IT Security > Anti-spam > /anti-spam-software/",
    "477. 21.1 > IT Security > Authentication > /authentication-software/",
    "478. 21.2 > IT Security > Cloud Security > /cloud-security-software/",
    "479. 21.3 > IT Security > Computer Security > /computer-security-software/",
    "480. 21.4 > IT Security > Cybersecurity > /cybersecurity-software/",
    "481. 21.5 > IT Security > Email Security > /email-security-software/",
    "482. 21.6 > IT Security > Endpoint Detection and Response (EDR) > /endpoint-detection-and-response-software/",
    "483. 21.7 > IT Security > Endpoint Protection > /endpoint-protection-software/",
    "484. 21.8 > IT Security > Network Security > /network-security-software/",
    "485. 21.9 > IT Security > Password Management > /password-management-software/",
    "486. 21.10 > IT Security > Privileged Access Management > /privileged-access-management-software/",
    "487. 21.11 > IT Security > SIEM > /siem-software/",
    "488. 21.12 > IT Security > Single Sign On (SSO) > /single-sign-on-software/",
    "489. 21.13 > IT Security > Vulnerability Management > /vulnerability-management-software/",
    "490. 22.0 > Legal & Law Enforcement > Conflict Checking > /conflict-checking-software/",
    "491. 22.1 > Legal & Law Enforcement > Court Management > /court-management-software/",
    "492. 22.2 > Legal & Law Enforcement > Digital Rights Management > /digital-rights-management-software/",
    "493. 22.3 > Legal & Law Enforcement > Docketing > /docketing-software/",
    "494. 22.4 > Legal & Law Enforcement > Electronic Discovery > /electronic-discovery-software/",
    "495. 22.5 > Legal & Law Enforcement > Emergency Notification > /emergency-notification-software/",
    "496. 22.6 > Legal & Law Enforcement > Entity Management > /entity-management-software/",
    "497. 22.7 > Legal & Law Enforcement > Intellectual Property Management > /intellectual-property-management-software/",
    "498. 22.8 > Legal & Law Enforcement > Investigation Management > /investigation-management-software/",
    "499. 22.9 > Legal & Law Enforcement > Jail Management > /jail-management-software/",
    "500. 22.10 > Legal & Law Enforcement > Law Enforcement > /law-enforcement-software/",
    "501. 22.11 > Legal & Law Enforcement > Law Practice Management > /law-practice-management-software/",
    "502. 22.12 > Legal & Law Enforcement > Legal Billing > /legal-billing-software/",
    "503. 22.13 > Legal & Law Enforcement > Legal Calendar > /legal-calendar-software/",
    "504. 22.14 > Legal & Law Enforcement > Legal Case Management > /legal-case-management-software/",
    "505. 22.15 > Legal & Law Enforcement > Legal Document Management > /legal-document-management-software/",
    "506. 22.16 > Legal & Law Enforcement > Legal Research > /legal-research-software/",
    "507. 22.17 > Legal & Law Enforcement > Trust Accounting > /trust-accounting-software/",
    "508. 23.0 > Logistics & Supply Chain >  Shipping > /shipping-software/",
    "509. 23.1 > Logistics & Supply Chain > Barcoding > /barcoding-software/",
    "510. 23.2 > Logistics & Supply Chain > Courier > /courier-software/",
    "511. 23.3 > Logistics & Supply Chain > Delivery Management > /delivery-management-software/",
    "512. 23.4 > Logistics & Supply Chain > Demand Planning > /demand-planning-software/",
    "513. 23.5 > Logistics & Supply Chain > Distribution > /distribution-software/",
    "514. 23.6 > Logistics & Supply Chain > Dock Scheduling > /dock-scheduling-software/",
    "515. 23.7 > Logistics & Supply Chain > Dropshipping > /dropshipping-software/",
    "516. 23.8 > Logistics & Supply Chain > Fleet Maintenance > /fleet-maintenance-software/",
    "517. 23.9 > Logistics & Supply Chain > Fleet Management > /fleet-management-software/",
    "518. 23.10 > Logistics & Supply Chain > Freight > /freight-software/",
    "519. 23.11 > Logistics & Supply Chain > Fuel Management > /fuel-management-software/",
    "520. 23.12 > Logistics & Supply Chain > GPS Tracking > /gps-tracking-software/",
    "521. 23.13 > Logistics & Supply Chain > Inventory Management > /inventory-management-software/",
    "522. 23.14 > Logistics & Supply Chain > Logistics > /logistics-software/",
    "523. 23.15 > Logistics & Supply Chain > Marine > /marine-software/",
    "524. 23.16 > Logistics & Supply Chain > Moving > /moving-software/",
    "525. 23.17 > Logistics & Supply Chain > Packaging > /packaging-software/",
    "526. 23.18 > Logistics & Supply Chain > Parcel Audit > /parcel-audit-software/",
    "527. 23.19 > Logistics & Supply Chain > Parking Management > /parking-management-software/",
    "528. 23.20 > Logistics & Supply Chain > Public Transportation > /public-transportation-software/",
    "529. 23.21 > Logistics & Supply Chain > Route Planning > /route-planning-software/",
    "530. 23.22 > Logistics & Supply Chain > School Bus Routing > /school-bus-routing-software/",
    "531. 23.23 > Logistics & Supply Chain > Shipment Tracking > /shipment-tracking-software/",
    "532. 23.24 > Logistics & Supply Chain > Supply Chain Management > /supply-chain-management-software/",
    "533. 23.25 > Logistics & Supply Chain > Towing > /towing-software/",
    "534. 23.26 > Logistics & Supply Chain > Transportation Dispatch > /transportation-dispatch-software/",
    "535. 23.27 > Logistics & Supply Chain > Transportation Management > /transportation-management-software/",
    "536. 23.28 > Logistics & Supply Chain > Trucking > /trucking-software/",
    "537. 23.29 > Logistics & Supply Chain > Vendor Management > /vendor-management-software/",
    "538. 23.30 > Logistics & Supply Chain > Warehouse Management > /warehouse-management-software/",
    "539. 23.31 > Logistics & Supply Chain > Yard Management > /yard-management-software/",
    "540. 24.0 > Maintenance > Auto Body > /auto-body-software/",
    "541. 24.1 > Maintenance > Auto Repair > /auto-repair-software/",
    "542. 24.2 > Maintenance > Aviation Maintenance > /aviation-maintenance-software/",
    "543. 24.3 > Maintenance > Building Maintenance > /building-maintenance-software/",
    "544. 24.4 > Maintenance > CMMS > /cmms-software/",
    "545. 24.5 > Maintenance > Equipment Maintenance > /equipment-maintenance-software/",
    "546. 24.6 > Maintenance > Maintenance Management > /maintenance-management-software/",
    "547. 24.7 > Maintenance > Preventive Maintenance > /preventive-maintenance-software/",
    "548. 24.8 > Maintenance > Tool Management > /tool-management-software/",
    "549. 25.0 > Manufacturing & Engineering > BIM > /bim-software/",
    "550. 25.1 > Manufacturing & Engineering > Calibration Management > /calibration-management-software/",
    "551. 25.2 > Manufacturing & Engineering > Chemical > /chemical-software/",
    "552. 25.3 > Manufacturing & Engineering > Electrical Design > /electrical-design-software/",
    "553. 25.4 > Manufacturing & Engineering > Engineering CAD > /engineering-cad-software/",
    "554. 25.5 > Manufacturing & Engineering > Job Shop > /job-shop-software/",
    "555. 25.6 > Manufacturing & Engineering > Manufacturing > /manufacturing-execution-software/",
    "556. 25.7 > Manufacturing & Engineering > Manufacturing Execution > /manufacturing-execution-software/",
    "557. 25.8 > Manufacturing & Engineering > MRP > /mrp-software/",
    "558. 25.9 > Manufacturing & Engineering > OEE > /oee-software/",
    "559. 25.10 > Manufacturing & Engineering > Product Configurator > /product-configurator-software/",
    "560. 25.11 > Manufacturing & Engineering > Product Data Management > /product-data-management-software/",
    "561. 25.12 > Manufacturing & Engineering > Production Scheduling > /production-scheduling-software/",
    "562. 25.13 > Manufacturing & Engineering > Quality Management > /quality-management-software/",
    "563. 25.14 > Manufacturing & Engineering > SCADA > /scada-software/",
    "564. 25.15 > Manufacturing & Engineering > Simulation > /simulation-software/",
    "565. 25.16 > Manufacturing & Engineering > SPC > /spc-software/",
    "566. 26.0 > Marketing & Digital Marketing > Account Based Marketing > /account-based-marketing-software/",
    "567. 26.1 > Marketing & Digital Marketing > Ad Server > /ad-server-software/",
    "568. 26.2 > Marketing & Digital Marketing > Advertising Agency > /advertising-agency-software/",
    "569. 26.3 > Marketing & Digital Marketing > Affiliate > /affiliate-software/",
    "570. 26.4 > Marketing & Digital Marketing > App Store Optimization Tools (ASO) > /app-store-optimization-tools-software/",
    "571. 26.5 > Marketing & Digital Marketing > Brand Management > /brand-management-software/",
    "572. 26.6 > Marketing & Digital Marketing > Brand Protection > /brand-protection-software/",
    "573. 26.7 > Marketing & Digital Marketing > Campaign Management > /campaign-management-software/",
    "574. 26.8 > Marketing & Digital Marketing > Click Fraud > /click-fraud-software/",
    "575. 26.9 > Marketing & Digital Marketing > Content Marketing > /content-marketing-software/",
    "576. 26.10 > Marketing & Digital Marketing > Contest > /contest-software/",
    "577. 26.11 > Marketing & Digital Marketing > Conversational Marketing Platform > /conversational-marketing-platform-software/",
    "578. 26.12 > Marketing & Digital Marketing > Customer Data Platform > /customer-data-platform-software/",
    "579. 26.13 > Marketing & Digital Marketing > Direct Mail Automation > /direct-mail-automation-software/",
    "580. 26.14 > Marketing & Digital Marketing > Email Marketing > /email-marketing-software/",
    "581. 26.15 > Marketing & Digital Marketing > Email Tracking > /email-tracking-software/",
    "582. 26.16 > Marketing & Digital Marketing > Email Verification Tools > /email-verification-tools-software/",
    "583. 26.17 > Marketing & Digital Marketing > Influencer Marketing > /influencer-marketing-software/",
    "584. 26.18 > Marketing & Digital Marketing > Landing Page > /landing-page-software/",
    "585. 26.19 > Marketing & Digital Marketing > Lead Generation > /lead-generation-software/",
    "586. 26.20 > Marketing & Digital Marketing > Link Management Tools > /link-management-tools-software/",
    "587. 26.21 > Marketing & Digital Marketing > Market Research > /market-research-software/",
    "588. 26.22 > Marketing & Digital Marketing > Marketing Analytics > /marketing-analytics-software/",
    "589. 26.23 > Marketing & Digital Marketing > Marketing Attribution > /marketing-attribution-software/",
    "590. 26.24 > Marketing & Digital Marketing > Marketing Automation > /marketing-automation-software/",
    "591. 26.25 > Marketing & Digital Marketing > Marketing Planning > /marketing-planning-software/",
    "592. 26.26 > Marketing & Digital Marketing > Mobile Marketing > /mobile-marketing-software/",
    "593. 26.27 > Marketing & Digital Marketing > MRM > /mrm-software/",
    "594. 26.28 > Marketing & Digital Marketing > Online Proofing > /online-proofing-software/",
    "595. 26.29 > Marketing & Digital Marketing > Personalization > /personalization-software/",
    "596. 26.30 > Marketing & Digital Marketing > PPC > /ppc-software/",
    "597. 26.31 > Marketing & Digital Marketing > Public Relations > /public-relations-software/",
    "598. 26.32 > Marketing & Digital Marketing > Push Notifications > /push-notifications-software/",
    "599. 26.33 > Marketing & Digital Marketing > Reputation Management > /reputation-management-software/",
    "600. 26.34 > Marketing & Digital Marketing > Retargeting > /retargeting-software/",
    "601. 26.35 > Marketing & Digital Marketing > Review Management > /review-management-software/",
    "602. 26.36 > Marketing & Digital Marketing > SMS Marketing > /sms-marketing-software/",
    "603. 26.37 > Marketing & Digital Marketing > Social Media Analytics Tools > /social-media-analytics-tools-software/",
    "604. 26.38 > Marketing & Digital Marketing > Social Media Management > /social-media-management-software/",
    "605. 26.39 > Marketing & Digital Marketing > Social Media Marketing > /social-media-marketing-software/",
    "606. 26.40 > Marketing & Digital Marketing > Social Media Monitoring > /social-media-monitoring-software/",
    "607. 26.41 > Marketing & Digital Marketing > Social Networking > /social-networking-software/",
    "608. 26.42 > Marketing & Digital Marketing > Social Selling > /social-selling-software/",
    "609. 26.43 > Marketing & Digital Marketing > Survey > /survey-software/",
    "610. 26.44 > Marketing & Digital Marketing > Trade Promotion Management > /trade-promotion-management-software/",
    "611. 26.45 > Marketing & Digital Marketing > Transactional Email > /transactional-email-software/",
    "612. 27.0 > Nonprofit & Public Sector > Advocacy > /advocacy-software/",
    "613. 27.1 > Nonprofit & Public Sector > Association Management > /association-management-software/",
    "614. 27.2 > Nonprofit & Public Sector > Cemetery > /cemetery-software/",
    "615. 27.3 > Nonprofit & Public Sector > Church Accounting > /church-accounting-software/",
    "616. 27.4 > Nonprofit & Public Sector > Church Management > /church-management-software/",
    "617. 27.5 > Nonprofit & Public Sector > Church Presentation > /church-presentation-software/",
    "618. 27.6 > Nonprofit & Public Sector > Code Enforcement > /code-enforcement-software/",
    "619. 27.7 > Nonprofit & Public Sector > Donation Management > /donation-management-software/",
    "620. 27.8 > Nonprofit & Public Sector > Fire Department > /fire-department-software/",
    "621. 27.9 > Nonprofit & Public Sector > Fund Accounting > /fund-accounting-software/",
    "622. 27.10 > Nonprofit & Public Sector > Fundraising > /fundraising-software/",
    "623. 27.11 > Nonprofit & Public Sector > Government > /government-software/",
    "624. 27.12 > Nonprofit & Public Sector > Grant Management > /grant-management-software/",
    "625. 27.13 > Nonprofit & Public Sector > Human Services > /human-services-software/",
    "626. 27.14 > Nonprofit & Public Sector > Membership Management > /membership-management-software/",
    "627. 27.15 > Nonprofit & Public Sector > Municipal > /municipal-software/",
    "628. 27.16 > Nonprofit & Public Sector > Museum > /museum-software/",
    "629. 27.17 > Nonprofit & Public Sector > Nonprofit > /nonprofit-software/",
    "630. 27.18 > Nonprofit & Public Sector > Permit > /permit-software/",
    "631. 27.19 > Nonprofit & Public Sector > Political Campaign > /political-campaign-software/",
    "632. 27.20 > Nonprofit & Public Sector > Polling > /polling-software/",
    "633. 27.21 > Nonprofit & Public Sector > Public Works > /public-works-software/",
    "634. 27.22 > Nonprofit & Public Sector > Social Work Case Management > /social-work-case-management-software/",
    "635. 27.23 > Nonprofit & Public Sector > Volunteer Management > /volunteer-management-software/",
    "636. 27.24 > Nonprofit & Public Sector > Voting > /voting-software/",
    "637. 27.25 > Nonprofit & Public Sector > Worship > /worship-software/",
    "638. 28.0 > Product > AB Testing > /ab-testing-software/",
    "639. 28.1 > Product > Creative Management > /creative-management-software/",
    "640. 28.2 > Product > Customer Journey Mapping Tools > /customer-journey-mapping-tools-software/",
    "641. 28.3 > Product > Gamification > /gamification-software/",
    "642. 28.4 > Product > Graphic Design > /graphic-design-software/",
    "643. 28.5 > Product > Heatmap > /heatmap-software/",
    "644. 28.6 > Product > PIM > /pim-software/",
    "645. 28.7 > Product > Product Lifecycle Management > /product-lifecycle-management-software/",
    "646. 28.8 > Product > Product Management > /product-management-software/",
    "647. 28.9 > Product > Product Roadmap > /product-roadmap-software/",
    "648. 28.10 > Product > Prototyping > /prototyping-software/",
    "649. 28.11 > Product > UX > /ux-software/",
    "650. 28.12 > Product > Vector Graphics > /vector-graphics-software/",
    "651. 28.13 > Product > Wireframe > /wireframe-software/",
    "652. 29.0 > Project Management > Agile Project Management Tools > /agile-project-management-tools-software/",
    "653. 29.1 > Project Management > Bug Tracking > /bug-tracking-software/",
    "654. 29.2 > Project Management > Diagram > /diagram-software/",
    "655. 29.3 > Project Management > Gantt Chart > /gantt-chart-software/",
    "656. 29.4 > Project Management > Idea Management > /idea-management-software/",
    "657. 29.5 > Project Management > Innovation > /innovation-software/",
    "658. 29.6 > Project Management > Issue Tracking > /issue-tracking-software/",
    "659. 29.7 > Project Management > IT Project Management > /it-project-management-software/",
    "660. 29.8 > Project Management > Job Costing > /job-costing-software/",
    "661. 29.9 > Project Management > Kanban Tools > /kanban-tools-software/",
    "662. 29.10 > Project Management > Mind Mapping > /mind-mapping-software/",
    "663. 29.11 > Project Management > Professional Services Automation > /professional-services-automation-software/",
    "664. 29.12 > Project Management > Project Management > /project-management-software/",
    "665. 29.13 > Project Management > Project Planning > /project-planning-software/",
    "666. 29.14 > Project Management > Project Portfolio Management > /project-portfolio-management-software/",
    "667. 29.15 > Project Management > Project Tracking > /project-tracking-software/",
    "668. 29.16 > Project Management > Requirements Management > /requirements-management-software/",
    "669. 29.17 > Project Management > Resource Management > /resource-management-software/",
    "670. 29.18 > Project Management > Scrum > /scrum-software/",
    "671. 29.19 > Project Management > Spreadsheet > /spreadsheet-software/",
    "672. 29.20 > Project Management > Task Management > /task-management-software/",
    "673. 29.21 > Project Management > Time and Expense > /time-and-expense-software/",
    "674. 29.22 > Project Management > Time Tracking > /time-tracking-software/",
    "675. 29.23 > Project Management > Workflow Management > /workflow-management-software/",
    "676. 30.0 > Real Estate > Commercial Real Estate > /commercial-real-estate-software/",
    "677. 30.1 > Real Estate > HOA > /hoa-software/",
    "678. 30.2 > Real Estate > Lease Management > /lease-management-software/",
    "679. 30.3 > Real Estate > Real Estate Agency > /real-estate-agency-software/",
    "680. 30.4 > Real Estate > Real Estate CMA > /real-estate-cma-software/",
    "681. 30.5 > Real Estate > Real Estate CRM > /real-estate-crm-software/",
    "682. 30.6 > Real Estate > Real Estate Property Management > /real-estate-property-management-software/",
    "683. 30.7 > Real Estate > Real Estate Transaction Management > /real-estate-transaction-management-software/",
    "684. 30.8 > Real Estate > Rental Property Management > /rental-property-management-software/",
    "685. 30.9 > Real Estate > Virtual Tour > /virtual-tour-software/",
    "686. 31.0 > Recreation > Camp Management > /camp-management-software/",
    "687. 31.1 > Recreation > Campground Management > /campground-management-software/",
    "688. 31.2 > Recreation > Club Management > /club-management-software/",
    "689. 31.3 > Recreation > Dance Studio > /dance-studio-software/",
    "690. 31.4 > Recreation > Driving School > /driving-school-software/",
    "691. 31.5 > Recreation > Fitness > /fitness-software/",
    "692. 31.6 > Recreation > Golf Course > /golf-course-software/",
    "693. 31.7 > Recreation > Gymnastics > /gymnastics-software/",
    "694. 31.8 > Recreation > Martial Arts > /martial-arts-software/",
    "695. 31.9 > Recreation > Nutrition Analysis > /nutrition-analysis-software/",
    "696. 31.10 > Recreation > Nutritionist > /nutritionist-software/",
    "697. 31.11 > Recreation > Parks and Recreation > /parks-and-recreation-software/",
    "698. 31.12 > Recreation > Personal Trainer > /personal-trainer-software/",
    "699. 31.13 > Recreation > Pilates Studio > /pilates-studio-software/",
    "700. 31.14 > Recreation > Pool Service > /pool-service-software/",
    "701. 31.15 > Recreation > Sports League > /sports-league-software/",
    "702. 31.16 > Recreation > Swim School > /swim-school-software/",
    "703. 31.17 > Recreation > Yoga Studio > /yoga-studio-software/",
    "704. 32.0 > Retail & Consumer > Android Kiosk > /android-kiosk-software/",
    "705. 32.1 > Retail & Consumer > Apparel Management > /apparel-management-software/",
    "706. 32.2 > Retail & Consumer > Art Gallery > /art-gallery-software/",
    "707. 32.3 > Retail & Consumer > Auction > /auction-software/",
    "708. 32.4 > Retail & Consumer > Auto Dealer > /auto-dealer-software/",
    "709. 32.5 > Retail & Consumer > B2B Ecommerce Platform > /b2b-ecommerce-platform-software/",
    "710. 32.6 > Retail & Consumer > Barbershop > /barbershop-software/",
    "711. 32.7 > Retail & Consumer > Car Rental > /car-rental-software/",
    "712. 32.8 > Retail & Consumer > Catalog Management > /catalog-management-software/",
    "713. 32.9 > Retail & Consumer > Computer Repair Shop > /computer-repair-shop-software/",
    "714. 32.10 > Retail & Consumer > Consignment > /consignment-software/",
    "715. 32.11 > Retail & Consumer > Convenience Store > /convenience-store-software/",
    "716. 32.12 > Retail & Consumer > Customer Advocacy > /customer-advocacy-software/",
    "717. 32.13 > Retail & Consumer > Customer Loyalty > /customer-loyalty-software/",
    "718. 32.14 > Retail & Consumer > Dry Cleaning > /dry-cleaning-software/",
    "719. 32.15 > Retail & Consumer > eCommerce > /ecommerce-software/",
    "720. 32.16 > Retail & Consumer > Equipment Rental > /equipment-rental-software/",
    "721. 32.17 > Retail & Consumer > Fashion Design and Production > /fashion-design-and-production-software/",
    "722. 32.18 > Retail & Consumer > Florist > /florist-software/",
    "723. 32.19 > Retail & Consumer > Franchise Management > /franchise-management-software/",
    "724. 32.20 > Retail & Consumer > Funeral Home > /funeral-home-software/",
    "725. 32.21 > Retail & Consumer > Garden Center > /garden-center-software/",
    "726. 32.22 > Retail & Consumer > Inventory Control > /inventory-control-software/",
    "727. 32.23 > Retail & Consumer > iPad Kiosk > /ipad-kiosk-software/",
    "728. 32.24 > Retail & Consumer > iPad POS > /ipad-pos-software/",
    "729. 32.25 > Retail & Consumer > Jewelry Store Management > /jewelry-store-management-software/",
    "730. 32.26 > Retail & Consumer > Kennel > /kennel-software/",
    "731. 32.27 > Retail & Consumer > Kiosk > /kiosk-software/",
    "732. 32.28 > Retail & Consumer > Locksmith > /locksmith-software/",
    "733. 32.29 > Retail & Consumer > Lost and Found > /lost-and-found-software/",
    "734. 32.30 > Retail & Consumer > Marketplace > /marketplace-software/",
    "735. 32.31 > Retail & Consumer > Multi-Channel eCommerce > /multi-channel-ecommerce-software/",
    "736. 32.32 > Retail & Consumer > Order Entry > /order-entry-software/",
    "737. 32.33 > Retail & Consumer > Order Management > /order-management-software/",
    "738. 32.34 > Retail & Consumer > Pawn Shop > /pawn-shop-software/",
    "739. 32.35 > Retail & Consumer > Payment Processing > /payment-processing-software/",
    "740. 32.36 > Retail & Consumer > Photography Studio > /photography-studio-software/",
    "741. 32.37 > Retail & Consumer > Point of Sale > /point-of-sale-software/",
    "742. 32.38 > Retail & Consumer > Rental > /rental-software/",
    "743. 32.39 > Retail & Consumer > Retail Management Systems > /retail-management-systems-software/",
    "744. 32.40 > Retail & Consumer > Retail POS System > /retail-pos-system-software/",
    "745. 32.41 > Retail & Consumer > Sales Tax > /sales-tax-software/",
    "746. 32.42 > Retail & Consumer > Salon > /salon-software/",
    "747. 32.43 > Retail & Consumer > Self Storage > /self-storage-software/",
    "748. 32.44 > Retail & Consumer > Shopping Cart > /shopping-cart-software/",
    "749. 32.45 > Retail & Consumer > Small Business eCommerce > /small-business-ecommerce-software/",
    "750. 32.46 > Retail & Consumer > Small Business Loyalty Programs > /small-business-loyalty-programs-software/",
    "751. 32.47 > Retail & Consumer > Store Locator > /store-locator-software/",
    "752. 32.48 > Retail & Consumer > Tattoo Studio > /tattoo-studio-software/",
    "753. 32.49 > Retail & Consumer > Winery > /winery-software/",
    "754. 33.0 > Sales > Channel Management > /channel-management-software/",
    "755. 33.1 > Sales > Commission > /commission-software/",
    "756. 33.2 > Sales > CPQ > /cpq-software/",
    "757. 33.3 > Sales > Inside Sales > /inside-sales-software/",
    "758. 33.4 > Sales > Lead Capture > /lead-capture-software/",
    "759. 33.5 > Sales > Lead Management > /lead-management-software/",
    "760. 33.6 > Sales > Lead Nurturing > /lead-nurturing-software/",
    "761. 33.7 > Sales > MLM > /mlm-software/",
    "762. 33.8 > Sales > Pricing Optimization > /pricing-optimization-software/",
    "763. 33.9 > Sales > Proposal Management > /proposal-management-software/",
    "764. 33.10 > Sales > Quoting > /quoting-software/",
    "765. 33.11 > Sales > Referral > /referral-software/",
    "766. 33.12 > Sales > Sales Coaching > /sales-coaching-software/",
    "767. 33.13 > Sales > Sales Enablement > /sales-enablement-software/",
    "768. 33.14 > Sales > Sales Force Automation > /sales-force-automation-software/",
    "769. 33.15 > Sales > Sales Forecasting > /sales-forecasting-software/",
    "770. 33.16 > Sales > Telemarketing > /telemarketing-software/",
    "771. 33.17 > Sales > Warranty Management > /warranty-management-software/",
]
```
