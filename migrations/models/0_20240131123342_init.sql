-- upgrade --
CREATE TABLE IF NOT EXISTS "teams" (
    "team_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "users" (
    "user_id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "status" VARCHAR(8) NOT NULL
);
COMMENT ON COLUMN "users"."status" IS 'ACTIVE: active\nPENDING: pending\nINACTIVE: inactive';
CREATE TABLE IF NOT EXISTS "integrations" (
    "integration_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "token" VARCHAR(50) NOT NULL,
    "status" VARCHAR(8) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("user_id") ON DELETE CASCADE
);
COMMENT ON COLUMN "integrations"."status" IS 'ACTIVE: active\nINACTIVE: inactive';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "teams_memberships" (
    "teams_id" INT NOT NULL REFERENCES "teams" ("team_id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("user_id") ON DELETE CASCADE
);
