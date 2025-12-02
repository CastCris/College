PRAGMA foreign_keys = ON;

CREATE TABLE "User"(
    "id" CHAR(32) PRIMARY KEY,
    "userInfos_id" CHAR(32) NOT NULL UNIQUE,
    "userProfile_id" CHAR(32) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    FOREIGN KEY("userInfos_id") REFERENCES "UserInfos"("id"),
    FOREIGN KEY("userProfile_id") REFERENCES "UserProfile"("id")
);

CREATE TABLE "UserInfos"(
    "id" CHAR(32) PRIMARY KEY,
    "hashed_name" CHAR(32) NOT NULL,
    "hashed_email" CHAR(32) NOT NULL,
    "cipher_name" VARCHAR(255) NOT NULL,
    "cipher_email" VARCHAR(255) NOT NULL
);

CREATE TABLE "UserProfile"(
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(255) NOT NULL,
    "permissions" INTEGER NOT NULL
);

CREATE TABLE "Room"(
    "id" CHAR(32) PRIMARY KEY,
    "roomInfos_id" CHAR(32) NOT NULL UNIQUE,
    "roomType_id" CHAR(32) NOT NULL,
    FOREIGN KEY("roomInfos_id") REFERENCES "RoomInfos"("id"),
    FOREIGN KEY("roomType_id") REFERENCES "RoomType"("id")
);

CREATE TABLE "RoomInfos"(
    "id" CHAR(32) PRIMARY KEY,
    "hashed_tag" CHAR(32) NOT NULL,
    "hashed_location" CHAR(32) NOT NULL,
    "cipher_tag" VARCHAR(255) NOT NULL,
    "cipher_location" VARCHAR(255) NOT NULL
);

CREATE TABLE "RoomType"(
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(255) NOT NULL,
    "description" VARCHAR(155) NOT NULL,
    "capacity" INTEGER NOT NULL,
    "price" INTEGER NOT NULL
);

CREATE TABLE "RoomStatus"(
    "id" CHAR(32) PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);

CREATE TABLE "ReserveCandidate"(
    "id" CHAR(32) PRIMARY KEY,
    "room_id" CHAR(32) NOT NULL,
    "user_id" CHAR(32) NOT NULL UNIQUE,
    "reserve_id" CHAR(32) NOT NULL,
    "price" INTEGER NOT NULL,
    FOREIGN KEY("room_id") REFERENCES "Room"("id"),
    FOREIGN KEY("user_id") REFERENCES "User"("id"),
    FOREIGN KEY("reserve_id") REFERENCES "Reserve"("id")
);

CREATE TABLE "ReserveStatus"(
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);

CREATE TABLE "Reserve"(
    "id" CHAR(32) PRIMARY KEY,
    "reserveStatus_id" CHAR(32) NOT NULL,
    "chekin_date" TEXT NOT NULL,
    "chekout_date" TEXT NOT NULL,
    FOREIGN KEY("reserveStatus_id") REFERENCES "ReserveStatus"("id")
);

CREATE TABLE "Invoice"(
    "id" CHAR(32) PRIMARY KEY,
    "reserve_id" CHAR(32) NOT NULL,
    "emission_date" TEXT NOT NULL,
    "price" INTEGER NOT NULL,
    "daily_price" BIGINT NOT NULL,
    "status_id" CHAR(32) NOT NULL,
    FOREIGN KEY("status_id") REFERENCES "InvoiceStatus"("id"),
    FOREIGN KEY("reserve_id") REFERENCES "ReserveCandidate"("id")
);

CREATE TABLE "Service"(
    "id" CHAR(32) PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "price" INTEGER NOT NULL
);

CREATE TABLE "InvoiceItem"(
    "id" CHAR(32) PRIMARY KEY,
    "invoice_id" CHAR(32) NOT NULL,
    "service_id" CHAR(32) NOT NULL,
    "amount" INTEGER NOT NULL,
    "unit_value" INTEGER NOT NULL,
    "comsumption_date" TEXT NOT NULL,
    FOREIGN KEY("invoice_id") REFERENCES "Invoice"("id"),
    FOREIGN KEY("service_id") REFERENCES "Service"("id")
);

CREATE TABLE "InvoiceStatus"(
    "id" CHAR(32) PRIMARY KEY,
    "tag" VARCHAR(255) NOT NULL,
    "value" INTEGER NOT NULL
);

CREATE TABLE "RoomStatusItem"(
    "roomStatus_id" CHAR(32) NOT NULL,
    "room_id" CHAR(32) NOT NULL,
    PRIMARY KEY("roomStatus_id", "room_id"),
    FOREIGN KEY("roomStatus_id") REFERENCES "RoomStatus"("id"),
    FOREIGN KEY("room_id") REFERENCES "Room"("id")
);

