function is_script
{
    [[ $(file $1) = "$1: Bourne-Again shell script, ASCII text executable" ]] \
	&& echo "File $1 is a shell script"
}
