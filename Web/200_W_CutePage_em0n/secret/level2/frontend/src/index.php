<?php
    $url = $_GET["url"];
    $data = "";
    if (isset($url) && stripos($url, "flag") === false) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 2);
        curl_setopt($ch, CURLOPT_TIMEOUT, 5);
        $data = curl_exec($ch);
        curl_close($ch);
    }
?>
<html>
<head>
</head>
<body>
    <h1>Nhập một đường link, và chúng tôi sẽ giúp bạn hiển thị nó</h1>
    <h2>Chúng tôi đã thêm một số hạn chế vào tính năng này vì lý do bảo mật</h2>
    <h2>Thành thật xin lỗi vì sự bất tiện này</h2>
    <form>
    Link của bạn: <input name="url" placeholder="http://example.com">
    <button type="submit">Submit</button>
    </form>
    <?= $data ?>
</body>
<!-- Hãy tìm cách đọc nội dung của trang web http://flag:3000/flag -->
</html>