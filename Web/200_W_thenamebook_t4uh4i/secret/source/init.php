<?php
  $db = new SQLite3('db.db');
  $init_sql = <<<EOF
    CREATE TABLE user (
      id INT PRIMARY KEY NOT NULL,
      username TEXT NOT NULL,
      password TEXT NOT NULL
    );
  EOF;

  $db->exec($init_sql);

  function getFirstName($x) {
    $firstNames = ['Phu', 'Trung', 'Duy', 'Anh', 'Hai', 'Hung', 'Uyen', 'Tam', 'Huyen', 'Ngoc'];
    $x = $x * $x * $x + 3 * $x * $x + 5 * $x + 42;
    $x %= sizeof($firstNames);
    return $firstNames[$x];
  }

  function getLastName($x) {
    $lastNames = ['Nguyen', 'Le', 'Tran', 'Luong', 'Ly', 'Dao', 'Khau', 'Hoang'];
    $x = 2 * $x * $x * $x + 6 * $x * $x + 9 * $x + 69;
    $x %= sizeof($lastNames);
    return $lastNames[$x];
  }

  function getName($x) {
    if ($x === 69) {
      return 'ha?i';
    }
    return getFirstName($x) . getLastName($x);
  }

  function getPassword($x) {
    if ($x === 69) {
      return $_ENV['flag'];
    }
    return 'not here' . ($x % 2 === 1 ? '' : ' either');
  }

  $id = 0;
  $username = '';
  $password = '';

  $stmt = $db->prepare('INSERT INTO user VALUES (:id, :username, :password);');
  $stmt->bindParam(':id', $id, SQLITE3_INTEGER);
  $stmt->bindParam(':username', $username);
  $stmt->bindParam(':password', $password);

  for ($i = 1; $i <= 100; $i++) {
    $id = $i;
    $username = getName($i);
    $password = getPassword($i);
    $stmt->execute();
  }
?>