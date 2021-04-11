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
						followers,
						tweets,
						hashtags,
						mentions,
						retweets,
						likes;

-- ---------------------------------------------------------------------------
-- Table USERS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL PRIMARY KEY,
	email VARCHAR(50) NOT NULL UNIQUE,
	pass VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL UNIQUE,
	display_name TINYBLOB NOT NULL,
	location VARCHAR(150),
	description TINYBLOB,
	verified BOOLEAN DEFAULT FALSE,
	joined_on DATE DEFAULT (CURRENT_DATE)
);

-- ---------------------------------------------------------------------------
-- Table FOLLOWERS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS followers (
	follower_id SERIAL PRIMARY KEY,	
	following_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (following_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table TWEET
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS tweets (
	tweet_id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	reply_id BIGINT UNSIGNED,
	quote_id BIGINT UNSIGNED,
	content TINYBLOB NOT NULL,
	posted_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	edited_on DATETIME NULL ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (reply_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (quote_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table HASHTAGS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS hashtags (
	hashtag_id SERIAL PRIMARY KEY,
	tweet_id BIGINT UNSIGNED NOT NULL,
	hashtag VARCHAR(100) NOT NULL,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table MENTIONS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS mentions (
	mention_id SERIAL PRIMARY KEY,
	tweet_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table RETWEETS
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS retweets (
	retweet_id SERIAL PRIMARY KEY,
	tweet_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	retweeted_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- Table LIKES
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS likes (
	like_id SERIAL PRIMARY KEY,
	tweet_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	liked_on DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------
-- 
-- ---------------------------------------------------------------------------




