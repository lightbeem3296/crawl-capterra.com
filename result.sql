CREATE TABLE IF NOT EXISTS `Category` (
	`Category_ID` integer primary key NOT NULL UNIQUE,
	`Category_Name` TEXT,
	`Parent_Category_Name` TEXT,
	`Slug` TEXT
);
CREATE TABLE IF NOT EXISTS `Product` (
	`Product_ID` integer primary key NOT NULL UNIQUE,
	`Product_Name` TEXT,
	`Slug` TEXT,
	`Description` TEXT,
	`Rating_Score` REAL,
	`Reviews_Count` INTEGER,
	`URL` TEXT,
	`Recommendation_Percentage` REAL
);
CREATE TABLE IF NOT EXISTS `ProductCategory` (
	`id` integer primary key NOT NULL UNIQUE,
	`Product_ID` INTEGER NOT NULL,
	`Category_ID` INTEGER NOT NULL,
FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`),
FOREIGN KEY(`Category_ID`) REFERENCES `Category`(`Category_ID`)
);
CREATE TABLE IF NOT EXISTS `Review` (
	`Review_ID` integer primary key NOT NULL UNIQUE,
	`User` TEXT,
	`Content` TEXT,
	`Rating` REAL,
	`Product_ID` INTEGER,
FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`)
);


FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`)
FOREIGN KEY(`Category_ID`) REFERENCES `Category`(`Category_ID`)
FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`)
