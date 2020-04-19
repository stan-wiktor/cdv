#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>


int main(int argc, char *argv[])
{
    char buf1[] = "abcdefghij";
    char buf2[] = "ABCDEFGHIJ";

    int fd;
    if ((fd = open("file_hole.txt", O_CREAT | O_TRUNC | O_WRONLY, 0644)) == -1)
    {
        perror("create");
        return 1;
    }
    write(fd, buf1, 10);
    lseek(fd, 0, SEEK_SET)
    write(fd, buf2, 10);
    close(fd);
    return 0;
}