CREATE TABLE "User"(
    "id" CHAR(32) NOT NULL,
    "userInfos_id" CHAR(32) NOT NULL,
    "phashed_password" VARCHAR(255) NOT NULL,
    "permissions" INTEGER NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
ALTER TABLE
    "User" ADD CONSTRAINT "user_userinfos_id_unique" UNIQUE("userInfos_id");
CREATE TABLE "UserInfos"(
    "dek" CHAR(80) NOT NULL,
    "id" CHAR(32) NOT NULL,
    "hashed_name" CHAR(44) NOT NULL,
    "hashed_email" CHAR(44) NOT NULL,
    "cipher_name" VARCHAR(255) NOT NULL,
    "cipher_email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "UserInfos" ADD PRIMARY KEY("id");
CREATE TABLE "UserPermission"(
    "tag" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);
ALTER TABLE
    "UserPermission" ADD CONSTRAINT "userpermission_tag_unique" UNIQUE("tag");
ALTER TABLE
    "UserPermission" ADD PRIMARY KEY("value");
CREATE TABLE "Room"(
    "id" CHAR(32) NOT NULL,
    "roomInfos_id" CHAR(32) NOT NULL,
    "roomType_id" CHAR(32) NOT NULL,
    "status_value" INTEGER NOT NULL
);
ALTER TABLE
    "Room" ADD PRIMARY KEY("id");
ALTER TABLE
    "Room" ADD CONSTRAINT "room_roominfos_id_unique" UNIQUE("roomInfos_id");
CREATE TABLE "RoomInfos"(
    "dek" CHAR(80) NOT NULL,
    "id" CHAR(32) NOT NULL,
    "hashed_tag" CHAR(44) NOT NULL,
    "hashed_location" CHAR(44) NOT NULL,
    "cipher_tag" VARCHAR(255) NOT NULL,
    "cipher_location" VARCHAR(255) NOT NULL,
    "addictional_notes" TEXT NULL
);
ALTER TABLE
    "RoomInfos" ADD PRIMARY KEY("id");
CREATE TABLE "RoomType"(
    "id" CHAR(32) NOT NULL,
    "tag" VARCHAR(255) NOT NULL,
    "description" VARCHAR(155) NOT NULL,
    "capacity" INTEGER NOT NULL,
    "price" INTEGER NOT NULL
);
ALTER TABLE
    "RoomType" ADD PRIMARY KEY("id");
CREATE TABLE "RoomStatus"(
    "name" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL,
    "positive" BOOLEAN NOT NULL
);
ALTER TABLE
    "RoomStatus" ADD PRIMARY KEY("value", "positive");
ALTER TABLE
    "RoomStatus" ADD CONSTRAINT "roomstatus_name_unique" UNIQUE("name");
CREATE TABLE "ReserveCandidate"(
    "id" CHAR(32) NOT NULL,
    "room_id" CHAR(32) NOT NULL,
    "user_id" CHAR(32) NOT NULL,
    "reserve_id" CHAR(32) NOT NULL,
    "price" INTEGER NOT NULL
);
ALTER TABLE
    "ReserveCandidate" ADD PRIMARY KEY("id");
ALTER TABLE
    "ReserveCandidate" ADD CONSTRAINT "reservecandidate_user_id_unique" UNIQUE("user_id");
CREATE TABLE "ReserveStatus"(
    "id" CHAR(32) NOT NULL,
    "tag" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);
ALTER TABLE
    "ReserveStatus" ADD PRIMARY KEY("id");
CREATE TABLE "Reserve"(
    "id" CHAR(32) NOT NULL,
    "reserveStatus_id" CHAR(32) NOT NULL,
    "chekin_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "chekout_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Reserve" ADD PRIMARY KEY("id");
CREATE TABLE "Invoice"(
    "id" CHAR(32) NOT NULL,
    "reserve_id" CHAR(32) NOT NULL,
    "emission_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "price" INTEGER NOT NULL,
    "daily_price" BIGINT NOT NULL,
    "status_id" CHAR(32) NOT NULL
);
ALTER TABLE
    "Invoice" ADD PRIMARY KEY("id");
CREATE TABLE "Service"(
    "id" CHAR(32) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "price" INTEGER NOT NULL
);
ALTER TABLE
    "Service" ADD PRIMARY KEY("id");
CREATE TABLE "InvoiceItem"(
    "id" CHAR(32) NOT NULL,
    "invoice_id" CHAR(32) NOT NULL,
    "service_id" CHAR(32) NOT NULL,
    "amount" INTEGER NOT NULL,
    "unit_value" INTEGER NOT NULL,
    "comsumption_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "InvoiceItem" ADD PRIMARY KEY("id");
CREATE TABLE "InvoiceStatus"(
    "id" CHAR(32) NOT NULL,
    "tag" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);
ALTER TABLE
    "InvoiceStatus" ADD PRIMARY KEY("id");
ALTER TABLE
    "InvoiceItem" ADD CONSTRAINT "invoiceitem_service_id_foreign" FOREIGN KEY("service_id") REFERENCES "Service"("id");
ALTER TABLE
    "Reserve" ADD CONSTRAINT "reserve_reservestatus_id_foreign" FOREIGN KEY("reserveStatus_id") REFERENCES "ReserveStatus"("id");
ALTER TABLE
    "ReserveCandidate" ADD CONSTRAINT "reservecandidate_room_id_foreign" FOREIGN KEY("room_id") REFERENCES "Room"("id");
ALTER TABLE
    "ReserveCandidate" ADD CONSTRAINT "reservecandidate_reserve_id_foreign" FOREIGN KEY("reserve_id") REFERENCES "Reserve"("id");
ALTER TABLE
    "Invoice" ADD CONSTRAINT "invoice_status_id_foreign" FOREIGN KEY("status_id") REFERENCES "InvoiceStatus"("id");
ALTER TABLE
    "Room" ADD CONSTRAINT "room_roominfos_id_foreign" FOREIGN KEY("roomInfos_id") REFERENCES "RoomInfos"("id");
ALTER TABLE
    "User" ADD CONSTRAINT "user_userinfos_id_foreign" FOREIGN KEY("userInfos_id") REFERENCES "UserInfos"("id");
ALTER TABLE
    "InvoiceItem" ADD CONSTRAINT "invoiceitem_invoice_id_foreign" FOREIGN KEY("invoice_id") REFERENCES "Invoice"("id");
ALTER TABLE
    "Invoice" ADD CONSTRAINT "invoice_reserve_id_foreign" FOREIGN KEY("reserve_id") REFERENCES "ReserveCandidate"("id");
ALTER TABLE
    "ReserveCandidate" ADD CONSTRAINT "reservecandidate_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "User"("id");
ALTER TABLE
    "Room" ADD CONSTRAINT "room_roomtype_id_foreign" FOREIGN KEY("roomType_id") REFERENCES "RoomType"("id");