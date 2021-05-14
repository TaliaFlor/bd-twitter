-- ---------------------------------------------------------------------------
-- Setup
-- ---------------------------------------------------------------------------

USE twitter;


-- ---------------------------------------------------------------------------
-- TWEETS QUANTITY PER USER
-- ---------------------------------------------------------------------------

SELECT
	u.username,
	COUNT(u.user_id) AS tweets_qty,
	t.posted_on
FROM tweets t
INNER JOIN users u
	ON t.user_id = u.user_id
GROUP BY u.user_id
;


-- ---------------------------------------------------------------------------
-- USERS LIKES PER DAY
-- ---------------------------------------------------------------------------

SELECT
	u.username,
	COUNT(DATE_FORMAT(l.liked_on,'%d/%m/%Y')) AS likes_per_day,
	DATE_FORMAT(l.liked_on,'%d/%m/%Y') AS day
FROM users u
LEFT JOIN likes l
	ON u.user_id = l.user_id
GROUP BY u.user_id
;


-- ---------------------------------------------------------------------------
-- ENTITIES PER TWEET
-- ---------------------------------------------------------------------------

SELECT 
	t.tweet_id,
	t.user_id,
	COUNT(h.hashtag_id) AS hashtag_qty,
	COUNT(m.mention_id) AS mention_qty
FROM tweets t 
JOIN hashtags h 
	ON t.tweet_id = h.tweet_id 
JOIN mentions m 
	ON t.tweet_id = m.tweet_id
GROUP BY t.tweet_id
;


-- ---------------------------------------------------------------------------
-- MOST POPULAR HASHTAGS
-- ---------------------------------------------------------------------------

SELECT h.hashtag, COUNT(*) AS qty
FROM tweets t 
JOIN hashtags h 
	ON t.tweet_id = h.tweet_id 
GROUP BY h.hashtag
ORDER BY COUNT(*) DESC
;












