/* brModelo_logicalModel - PostgreSQL */

CREATE TABLE "User" (
    "id" CHAR(32) PRIMARY KEY,
    "userInfos_id" CHAR(32) UNIQUE,
    "phashed_password" VARCHAR(255),
    "permissions" INTEGER
);

CREATE TABLE "UserInfos" (
    "dek" CHAR(80),
    "id" CHAR(32) PRIMARY KEY,
    "hashed_name" CHAR(44),
    "hashed_email" CHAR(44) UNIQUE,
    "cipher_name" VARCHAR(255),
    "cipher_email" VARCHAR(255)
);

CREATE TABLE "UserPermission" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "value" INTEGER
);

CREATE TABLE "Invoice" (
    "id" CHAR(32) PRIMARY KEY,
    "reserveCandidate_id" CHAR(32),
    "emission_date" TIMESTAMP,
    "price" INTEGER,
    "daily_price" INTEGER,
    "status_id" CHAR(32)
);

CREATE TABLE "Room" (
    "dek" CHAR(80),
    "id" CHAR(32) PRIMARY KEY,
    "roomLocation_id" CHAR(32),
    "roomType_id" CHAR(32),
    "status_value" INTEGER,
    "hashed_tag" CHAR(44) UNIQUE,
    "cipher_tag" VARCHAR(255)
);

CREATE TABLE "InvoiceStatus" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "value" INTEGER
);

CREATE TABLE "InvoiceItem" (
    "id" CHAR(32) PRIMARY KEY,
    "invoice_id" CHAR(32),
    "service_id" CHAR(32),
    "amount" INTEGER,
    "unit_value" INTEGER,
    "comsumption_date" TIMESTAMP
);

CREATE TABLE "Service" (
    "id" CHAR(32) PRIMARY KEY,
    "name" CHAR(155),
    "price" INTEGER
);

CREATE TABLE "RoomType" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "description" TEXT,
    "capacity" SMALLINT,
    "price" SMALLINT
);

CREATE TABLE "RoomStatus" (
    "tag" VARCHAR(255) UNIQUE,
    "value" INTEGER,
    "positive" BOOLEAN,
    PRIMARY KEY ("positive", "value")
);

CREATE TABLE "ReserveCandidate" (
    "id" CHAR(32) PRIMARY KEY,
    "room_id" CHAR(32),
    "user_id" CHAR(32) UNIQUE,
    "reserve_id" CHAR(32),
    "price" INTEGER
);

CREATE TABLE "Reserve" (
    "id" CHAR(32) PRIMARY KEY,
    "reserveStatus_id" CHAR(32),
    "checkin_date" TIMESTAMP,
    "checkout_date" TIMESTAMP
);

CREATE TABLE "ReserveStatus" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155)
);

CREATE TABLE "RoomLocation" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155) UNIQUE,
    "tag_prefix" VARCHAR(5),
    "tag_suffix" VARCHAR(5)
);

-- Foreign Keys

ALTER TABLE "User"
ADD CONSTRAINT "FK_User_3"
FOREIGN KEY ("userInfos_id")
REFERENCES "UserInfos" ("id");

ALTER TABLE "Invoice"
ADD CONSTRAINT "FK_Invoice_1"
FOREIGN KEY ("status_id")
REFERENCES "InvoiceStatus" ("id");

ALTER TABLE "Invoice"
ADD CONSTRAINT "FK_Invoice_3"
FOREIGN KEY ("reserveCandidate_id")
REFERENCES "ReserveCandidate" ("id");

ALTER TABLE "Room"
ADD CONSTRAINT "FK_Room_2"
FOREIGN KEY ("roomType_id")
REFERENCES "RoomType" ("id");

ALTER TABLE "Room"
ADD CONSTRAINT "FK_Room_3"
FOREIGN KEY ("roomLocation_id")
REFERENCES "RoomLocation" ("id");

ALTER TABLE "InvoiceItem"
ADD CONSTRAINT "FK_InvoiceItem_2"
FOREIGN KEY ("invoice_id")
REFERENCES "Invoice" ("id");

ALTER TABLE "InvoiceItem"
ADD CONSTRAINT "FK_InvoiceItem_3"
FOREIGN KEY ("service_id")
REFERENCES "Service" ("id");

ALTER TABLE "ReserveCandidate"
ADD CONSTRAINT "FK_ReserveCandidate_1"
FOREIGN KEY ("room_id")
REFERENCES "Room" ("id");

ALTER TABLE "ReserveCandidate"
ADD CONSTRAINT "FK_ReserveCandidate_3"
FOREIGN KEY ("reserve_id")
REFERENCES "Reserve" ("id");

ALTER TABLE "ReserveCandidate"
ADD CONSTRAINT "FK_ReserveCandidate_4"
FOREIGN KEY ("user_id")
REFERENCES "User" ("id");

ALTER TABLE "Reserve"
ADD CONSTRAINT "FK_Reserve_2"
FOREIGN KEY ("reserveStatus_id")
REFERENCES "ReserveStatus" ("id");

