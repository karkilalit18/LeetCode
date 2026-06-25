# Write your MySQL query statement below
select contest_id,ROUND((COUNT(DISTINCT r.user_id) / (SELECT COUNT(user_id) FROM Users)) * 100, 2) as percentage from users u
right join register r
on u.user_id=r.user_id
group by r.contest_id
order by percentage desc,contest_id