/* brModelo_logicalModel - PostgreSQL */

CREATE TABLE "UserInfos" (
    "id" CHAR(32) PRIMARY KEY,
    "dek" CHAR(80),
    "hashed_name" CHAR(44),
    "hashed_email" CHAR(44) UNIQUE,
    "cipher_name" VARCHAR(255),
    "cipher_email" VARCHAR(255)
);

CREATE TABLE "User" (
    "id" CHAR(32) PRIMARY KEY,
    "userInfos_id" CHAR(32) UNIQUE,
    "phashed_password" VARCHAR(255),
    "permissions" INTEGER
);

CREATE TABLE "UserPermission" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "value" INTEGER
);

CREATE TABLE "InvoiceStatus" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "value" INTEGER
);

CREATE TABLE "RoomType" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155),
    "description" TEXT,
    "capacity" SMALLINT,
    "price" SMALLINT
);

CREATE TABLE "RoomLocation" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155) UNIQUE,
    "tag_prefix" VARCHAR(5),
    "tag_suffix" VARCHAR(5)
);

CREATE TABLE "RoomStatus" (
    "id" CHAR(16),
    "tag" VARCHAR(255),
    "value" INTEGER,
    "positive" BOOLEAN,
    PRIMARY KEY ("positive", "value"),
    UNIQUE ("tag", "id")
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

CREATE TABLE "Service" (
    "id" CHAR(32) PRIMARY KEY,
    "name" VARCHAR(155),
    "price" INTEGER
);

CREATE TABLE "ReserveStatus" (
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(155)
);

CREATE TABLE "Reserve" (
    "id" CHAR(32) PRIMARY KEY,
    "reserveStatus_id" CHAR(32),
    "checkin_date" TIMESTAMP,
    "checkout_date" TIMESTAMP
);

CREATE TABLE "ReserveCandidate" (
    "id" CHAR(32) PRIMARY KEY,
    "room_id" CHAR(32),
    "user_id" CHAR(32) UNIQUE,
    "reserve_id" CHAR(32),
    "price" INTEGER
);

CREATE TABLE "Invoice" (
    "id" CHAR(32) PRIMARY KEY,
    "reserveCandidate_id" CHAR(32),
    "emission_date" TIMESTAMP,
    "price" INTEGER,
    "daily_price" INTEGER,
    "status_id" CHAR(32)
);

CREATE TABLE "InvoiceItem" (
    "id" CHAR(32) PRIMARY KEY,
    "invoice_id" CHAR(32),
    "service_id" CHAR(32),
    "amount" INTEGER,
    "unit_value" INTEGER,
    "comsumption_date" TIMESTAMP
);

-- =========================
-- FOREIGN KEYS
-- =========================

ALTER TABLE "User"
    ADD CONSTRAINT "FK_User_UserInfos"
    FOREIGN KEY ("userInfos_id")
    REFERENCES "UserInfos" ("id");

ALTER TABLE "Invoice"
    ADD CONSTRAINT "FK_Invoice_Status"
    FOREIGN KEY ("status_id")
    REFERENCES "InvoiceStatus" ("id");

ALTER TABLE "Invoice"
    ADD CONSTRAINT "FK_Invoice_ReserveCandidate"
    FOREIGN KEY ("reserveCandidate_id")
    REFERENCES "ReserveCandidate" ("id");

ALTER TABLE "Room"
    ADD CONSTRAINT "FK_Room_RoomType"
    FOREIGN KEY ("roomType_id")
    REFERENCES "RoomType" ("id");

ALTER TABLE "Room"
    ADD CONSTRAINT "FK_Room_RoomLocation"
    FOREIGN KEY ("roomLocation_id")
    REFERENCES "RoomLocation" ("id");

ALTER TABLE "InvoiceItem"
    ADD CONSTRAINT "FK_InvoiceItem_Invoice"
    FOREIGN KEY ("invoice_id")
    REFERENCES "Invoice" ("id");

ALTER TABLE "InvoiceItem"
    ADD CONSTRAINT "FK_InvoiceItem_Service"
    FOREIGN KEY ("service_id")
    REFERENCES "Service" ("id");

ALTER TABLE "ReserveCandidate"
    ADD CONSTRAINT "FK_ReserveCandidate_Room"
    FOREIGN KEY ("room_id")
    REFERENCES "Room" ("id");

ALTER TABLE "ReserveCandidate"
    ADD CONSTRAINT "FK_ReserveCandidate_Reserve"
    FOREIGN KEY ("reserve_id")
    REFERENCES "Reserve" ("id");

ALTER TABLE "ReserveCandidate"
    ADD CONSTRAINT "FK_ReserveCandidate_User"
    FOREIGN KEY ("user_id")
    REFERENCES "User" ("id");

ALTER TABLE "Reserve"
    ADD CONSTRAINT "FK_Reserve_ReserveStatus"
    FOREIGN KEY ("reserveStatus_id")
    REFERENCES "ReserveStatus" ("id");

