-- upgrade --
CREATE TABLE IF NOT EXISTS "teams" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "user_id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "status" VARCHAR(8) NOT NULL
);
COMMENT ON COLUMN "users"."status" IS 'ACTIVE: active\nINACTIVE: inactive\nPENDING: pending';
CREATE TABLE IF NOT EXISTS "teams_memberships" (
    "membership_id" SERIAL NOT NULL PRIMARY KEY,
    "team_id_id" INT NOT NULL REFERENCES "teams" ("id") ON DELETE CASCADE,
    "user_id_id" INT NOT NULL REFERENCES "users" ("user_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "integrations" (
    "integration_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "token" VARCHAR(50) NOT NULL,
    "status" VARCHAR(8) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("user_id") ON DELETE CASCADE
);
COMMENT ON COLUMN "integrations"."status" IS 'ACTIVE: active\nINACTIVE: inactive\nPENDING: pending';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
