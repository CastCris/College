PRAGMA foreign_keys = ON;

CREATE TABLE "User"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "userInfos_id" TEXT NOT NULL UNIQUE,
    "phashed_password" TEXT NOT NULL,
    "permissions" INTEGER NOT NULL,
    FOREIGN KEY("userInfos_id") REFERENCES "UserInfos"("id")
);

CREATE TABLE "UserInfos"(
    "dek" TEXT NOT NULL,
    "id" TEXT NOT NULL PRIMARY KEY,
    "hashed_name" TEXT NOT NULL,
    "hashed_email" TEXT NOT NULL,
    "cipher_name" TEXT NOT NULL,
    "cipher_email" TEXT NOT NULL
);

CREATE TABLE "UserPermission"(
    "tag" TEXT NOT NULL UNIQUE,
    "value" INTEGER NOT NULL PRIMARY KEY
);

CREATE TABLE "Room"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "roomInfos_id" TEXT NOT NULL UNIQUE,
    "roomType_id" TEXT NOT NULL,
    "status_value" INTEGER NOT NULL,
    FOREIGN KEY("roomInfos_id") REFERENCES "RoomInfos"("id"),
    FOREIGN KEY("roomType_id") REFERENCES "RoomType"("id")
);

CREATE TABLE "RoomInfos"(
    "dek" TEXT NOT NULL,
    "id" TEXT NOT NULL PRIMARY KEY,
    "hashed_tag" TEXT NOT NULL,
    "hashed_location" TEXT NOT NULL,
    "cipher_tag" TEXT NOT NULL,
    "cipher_location" TEXT NOT NULL,
    "addictional_notes" TEXT
);

CREATE TABLE "RoomType"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "tag" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "capacity" INTEGER NOT NULL,
    "price" INTEGER NOT NULL
);

CREATE TABLE "RoomStatus"(
    "name" TEXT NOT NULL UNIQUE,
    "value" INTEGER NOT NULL,
    "positive" INTEGER NOT NULL,
    PRIMARY KEY("value", "positive")
);

CREATE TABLE "ReserveCandidate"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "room_id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL UNIQUE,
    "reserve_id" TEXT NOT NULL,
    "price" INTEGER NOT NULL,
    FOREIGN KEY("room_id") REFERENCES "Room"("id"),
    FOREIGN KEY("reserve_id") REFERENCES "Reserve"("id"),
    FOREIGN KEY("user_id") REFERENCES "User"("id")
);

CREATE TABLE "ReserveStatus"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "tag" TEXT NOT NULL,
    "value" INTEGER NOT NULL
);

CREATE TABLE "Reserve"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "reserveStatus_id" TEXT NOT NULL,
    "chekin_date" TEXT NOT NULL,
    "chekout_date" TEXT NOT NULL,
    FOREIGN KEY("reserveStatus_id") REFERENCES "ReserveStatus"("id")
);

CREATE TABLE "Invoice"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "reserve_id" TEXT NOT NULL,
    "emission_date" TEXT NOT NULL,
    "price" INTEGER NOT NULL,
    "daily_price" INTEGER NOT NULL,
    "status_id" TEXT NOT NULL,
    FOREIGN KEY("status_id") REFERENCES "InvoiceStatus"("id"),
    FOREIGN KEY("reserve_id") REFERENCES "ReserveCandidate"("id")
);

CREATE TABLE "Service"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "price" INTEGER NOT NULL
);

CREATE TABLE "InvoiceItem"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "invoice_id" TEXT NOT NULL,
    "service_id" TEXT NOT NULL,
    "amount" INTEGER NOT NULL,
    "unit_value" INTEGER NOT NULL,
    "comsumption_date" TEXT NOT NULL,
    FOREIGN KEY("service_id") REFERENCES "Service"("id"),
    FOREIGN KEY("invoice_id") REFERENCES "Invoice"("id")
);

CREATE TABLE "InvoiceStatus"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "tag" TEXT NOT NULL,
    "value" INTEGER NOT NULL
);

