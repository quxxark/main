import subprocess, os


SERVER_PATH = ''  # Path to the server.py file


class HttpServer:
    """
        The example of pytest-fixture (conftest.py):

            @pytest.fixture(scope='module')
            def startHttpServer():
                serverStart = HttpServer.start()
                httpServer = HttpServer()
                yield
                httpServer.stop()
    """

    @classmethod
    def start(cls):
        os.chmod(SERVER_PATH, 0o755)
        cls.server = subprocess.Popen(SERVER_PATH, stdout=subprocess.DEVNULL)

    def stop(self):
        if self.server.poll() is None:
            self.server.kill()
