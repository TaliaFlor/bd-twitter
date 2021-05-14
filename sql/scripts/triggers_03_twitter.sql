-- ---------------------------------------------------------------------------
-- Setup
-- ---------------------------------------------------------------------------

USE twitter;


-- ---------------------------------------------------------------------------
-- T_VALID_LOGIN
-- ---------------------------------------------------------------------------

DROP TRIGGER IF EXISTS T_INSERT_VALID_LOGIN
;
DELIMITER //
CREATE TRIGGER T_INSERT_VALID_LOGIN
	BEFORE INSERT ON users
	FOR EACH ROW 
	BEGIN
		  CALL SP_VALID_LOGIN(NEW.email, NEW.password);
	END
//
DELIMITER ;
;

DROP TRIGGER IF EXISTS T_UPDATE_VALID_LOGIN
;
DELIMITER //
CREATE TRIGGER T_UPDATE_VALID_LOGIN
	BEFORE UPDATE ON users
	FOR EACH ROW 
	BEGIN
		 CALL SP_VALID_LOGIN(NEW.email, NEW.password);
	END
//
DELIMITER ;
;


-- ---------------------------------------------------------------------------
-- T_ONE_HASHTAG_PER_ENTRY
-- ---------------------------------------------------------------------------

DROP TRIGGER IF EXISTS T_INSERT_ONE_HASHTAG_PER_ENTRY
;
DELIMITER //
CREATE TRIGGER T_INSERT_ONE_HASHTAG_PER_ENTRY
	BEFORE INSERT ON hashtags
	FOR EACH ROW 
	BEGIN
		CALL SP_ONE_HASHTAG_PER_ENTRY(NEW.hashtag);
	END
//
DELIMITER ;
;

DROP TRIGGER IF EXISTS T_UPDATE_ONE_HASHTAG_PER_ENTRY
;
DELIMITER //
CREATE TRIGGER T_UPDATE_ONE_HASHTAG_PER_ENTRY
	BEFORE UPDATE ON hashtags
	FOR EACH ROW 
	BEGIN
		CALL SP_ONE_HASHTAG_PER_ENTRY(NEW.hashtag);
	END
//
DELIMITER ;
;
















