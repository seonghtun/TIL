const express = require('express');
const router = express.Router();

const mysql      = require('mysql');
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '1234',
  database : 'express'
});

connection.connect();

// connection.query('SELECT * from Users', (error, rows, fields) => {
//  if (error) throw error;
//  console.log('User info is: ', rows);
// });

// connection.end();
// router.get('/', (req, res) => {
//  res.send(posts.data);
// });

router.get('/', (req, res) => {
	connection.query("SELECT * FROM NoticeBoard", (error, rows, fields) => {
	if (!rows) {
		res.status(400).send({message: '비어있습니다.'});
		return ;
		}
	res.send(rows);
	}
});

// 글 단일 조회
router.get('/:id', (req, res) => {
  connection.query('SELECT * from Users', (error, rows, fields) => {
  if (error) throw error;

  // TODO 글이 존재하는지 체크
  if (!rows) {
    res.status(400).send({ message: '존재하지 않는 글입니다.' });
    return;
  }
  res.send(rows);
  );
});

// 글 등록
router.post('/', (req, res) => {
  const { id, content } = req.body;
  var sql = "INSERT INTO NoticeBoard (user_id, content) VALUES ?";
  connection.query(sql, [body], (err, result) => {
  if (err) throw err;
  res.send({ message: '글을 등록했습니다.' });
  });
});

// 글 수정
router.put('/:id', (req, res) => {
  const { id, content } = req.body;

  // TODO id, title, content가 있는지 체크
  if (!req.params.id || !id || !content) {
    res.status(400).send({ message: 'id , content는 필수 입력 사항입니다.' });
    return;
  }
  var sql = $"update NoticeBoard set content = {content} where user_id = {id}";
  connection.query(sql, (err, result) => {
  if (err) throw err;
  res.send({ message: result.affectedRows + " record(s) updated"});
  });
});

// 글 삭제
router.delete('/:id', (req, res) => {
  if (!req.params.id) {
    res.status(400).send({ message: 'id는 필수 입력 사항입니다.' });
    return;
  }
	var sql = $"DELETE FROM NoticeBoard WHERE id = {req.body.content_id}";
	con.query(sql, function (err, result) {
    if (err) throw err;
    res.send({ "message" :"Number of records deleted: " + result.affectedRows);
  });
});

module.exports = router;
