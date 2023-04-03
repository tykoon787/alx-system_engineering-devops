# Setups an nginx server

# Install server
class { 'nginx':
  manage_repo => true,
}

$url = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$web_01='52.87.215.121'
nginx::resource::server { $web_01:
  listen_port       => '80',
  server_name       => $web_01,
  location          => {
    '/'             => {
      'content'     => '<html><body><p>"Hello World!</p></body></html>'
    }
    '/redirect_me'  => {
      'return'      => '301 $url'
    }
  }
}
