-- upgrade --
ALTER TABLE "users" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
ALTER TABLE "integrations" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
CREATE UNIQUE INDEX "uid_users_email_133a6f" ON "users" ("email");
-- downgrade --
DROP INDEX "idx_users_email_133a6f";
ALTER TABLE "users" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
ALTER TABLE "integrations" ALTER COLUMN "status" TYPE VARCHAR(8) USING "status"::VARCHAR(8);
