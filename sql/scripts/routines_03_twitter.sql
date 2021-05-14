-- ---------------------------------------------------------------------------
-- Setup
-- ---------------------------------------------------------------------------

USE twitter;


-- ---------------------------------------------------------------------------
-- SP_LOGIN
-- ---------------------------------------------------------------------------

DROP PROCEDURE IF EXISTS SP_VALID_LOGIN
;
DELIMITER //
CREATE PROCEDURE SP_VALID_LOGIN
	(IN IN_EMAIL VARCHAR(50), IN IN_PASSWORD VARCHAR(50))
	BEGIN
		DECLARE VAR_EMAIL_OR_PASSWORD_NULL BOOL;
		SET VAR_EMAIL_OR_PASSWORD_NULL = IN_EMAIL IS NULL OR IN_PASSWORD IS NULL;
		IF VAR_EMAIL_OR_PASSWORD_NULL THEN
			SIGNAL SQLSTATE '04000'	-- Para o fluxo
			SET MESSAGE_TEXT = 'Email and password are required fields';
		  END IF;
	END;
//
DELIMITER ;
;


-- ---------------------------------------------------------------------------
-- SP_ONE_HASHTAG_PER_ENTRY
-- ---------------------------------------------------------------------------

DROP PROCEDURE IF EXISTS SP_ONE_HASHTAG_PER_ENTRY
;
DELIMITER //
CREATE PROCEDURE SP_ONE_HASHTAG_PER_ENTRY
	(IN IN_HASHTAG VARCHAR(100))
	BEGIN 
		IF IN_HASHTAG LIKE '% %' THEN
			SIGNAL SQLSTATE '04000'	-- Para o fluxo
			SET MESSAGE_TEXT = 'Only one hashtag per entry is permited';
		  END IF;
	END;
//
DELIMITER ;
;











