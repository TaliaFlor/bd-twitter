-- ---------------------------------------------------------------------------
-- Schema TWITTER
-- ---------------------------------------------------------------------------

DROP SCHEMA IF EXISTS twitter;
CREATE SCHEMA twitter DEFAULT CHARACTER SET utf8;
USE twitter;

-- ---------------------------------------------------------------------------
-- Setup tables
-- ---------------------------------------------------------------------------

SET @@time_zone = 'SYSTEM';

DROP TABLE IF EXISTS users,
						tweets,
						comments,
						retweets,
						likes,
						followers;

-- ---------------------------------------------------------------------------
-- Table USERS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL PRIMARY KEY,
	email VARCHAR(50) NOT NULL UNIQUE,
	pass varchar(50) NOT NULL,
	username varchar(50) NOT NULL UNIQUE,
	display_name varchar(50) NOT NULL,
	joined_on DATE DEFAULT (CURRENT_DATE)
);

-- ---------------------------------------------------------------------------
-- Table TWEET
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS tweets (
	tweet_id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	content VARCHAR(280) NOT NULL,
	posted_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	edited_on DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table COMMENTS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS comments (
	comment_id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	tweet_id BIGINT UNSIGNED NOT NULL,
	posted_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	edited_on DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table RETWEETS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS retweets (
	retweet_id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	is_comment BOOLEAN NOT NULL,
	tweet_id BIGINT UNSIGNED,
	comment_id BIGINT UNSIGNED,
	retweeted_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (comment_id) REFERENCES comments(comment_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table LIKES
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS likes (
	like_id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	is_comment BOOLEAN NOT NULL,
	tweet_id BIGINT UNSIGNED,
	comment_id BIGINT UNSIGNED,
	liked_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (comment_id) REFERENCES comments(comment_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table FOLLOWERS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS followers (
	user_id BIGINT UNSIGNED NOT NULL,
	follower_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (follower_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- 
-- ---------------------------------------------------------------------------



