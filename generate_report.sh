echo "<html><body>"
echo "<table>"
echo "<tr>"
echo "<td>Filename</td> <td>Number of lines</td> <td>Average value</td>"
echo "</tr>"
for file in $@
do
	echo "<tr><td>${file}</td><td>$(cat ${file} | wc -l)</td><td>$(./average.py ${file})</td></tr>"
done
echo "</table>"
echo "</body></html>"
