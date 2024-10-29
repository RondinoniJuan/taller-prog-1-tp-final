curl https://gist.githubusercontent.com/sebiglesias/ea2faa92f4b25a79f811104584e91efb/raw/02378f041ae64d3d021031efeb1572cbddfc2fc7/test-web-server-log.txt > web-server-log.txt

grep " 200 " web-server-log.txt > ok.txt
grep " 500 " web-server-log.txt > errors.txt