CREATE TABLE "User"(
    "id" CHAR(32) NOT NULL,
    "userInfos_id" CHAR(32) NOT NULL,
    "userProfile_id" CHAR(32) NOT NULL,
    "password" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
ALTER TABLE
    "User" ADD CONSTRAINT "user_userinfos_id_unique" UNIQUE("userInfos_id");
CREATE TABLE "UserInfos"(
    "id" CHAR(32) NOT NULL,
    "hashed_name" CHAR(32) NOT NULL,
    "hashed_email" CHAR(32) NOT NULL,
    "cipher_name" VARCHAR(255) NOT NULL,
    "cipher_email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "UserInfos" ADD PRIMARY KEY("id");
CREATE TABLE "UserProfile"(
    "id" CHAR(32) NOT NULL,
    "tag" VARCHAR(255) NOT NULL,
    "permissions" INTEGER NOT NULL
);
ALTER TABLE
    "UserProfile" ADD PRIMARY KEY("id");
CREATE TABLE "Room"(
    "id" CHAR(32) NOT NULL,
    "roomInfos_id" CHAR(32) NOT NULL,
    "roomType_id" CHAR(32) NOT NULL,
    "roomStatus_id" CHAR(32) NOT NULL
);
ALTER TABLE
    "Room" ADD PRIMARY KEY("id");
ALTER TABLE
    "Room" ADD CONSTRAINT "room_roominfos_id_unique" UNIQUE("roomInfos_id");
CREATE TABLE "RoomInfos"(
    "id" CHAR(32) NOT NULL,
    "hashed_tag" CHAR(32) NOT NULL,
    "hashed_location" CHAR(32) NOT NULL,
    "cipher_name" VARCHAR(255) NOT NULL,
    "cipher_location" VARCHAR(255) NOT NULL
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
CREATE TABLE "Room_Status"(
    "id" CHAR(32) NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Room_Status" ADD PRIMARY KEY("id");
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
    "tag" VARCHAR(255) NOT NULL
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
    "tag" VARCHAR(255) NOT NULL
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
    "Room" ADD CONSTRAINT "room_roomstatus_id_foreign" FOREIGN KEY("roomStatus_id") REFERENCES "Room_Status"("id");
ALTER TABLE
    "InvoiceItem" ADD CONSTRAINT "invoiceitem_invoice_id_foreign" FOREIGN KEY("invoice_id") REFERENCES "Invoice"("id");
ALTER TABLE
    "User" ADD CONSTRAINT "user_userprofile_id_foreign" FOREIGN KEY("userProfile_id") REFERENCES "UserProfile"("id");
ALTER TABLE
    "Invoice" ADD CONSTRAINT "invoice_reserve_id_foreign" FOREIGN KEY("reserve_id") REFERENCES "ReserveCandidate"("id");
ALTER TABLE
    "ReserveCandidate" ADD CONSTRAINT "reservecandidate_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "User"("id");
ALTER TABLE
    "Room" ADD CONSTRAINT "room_roomtype_id_foreign" FOREIGN KEY("roomType_id") REFERENCES "RoomType"("id");