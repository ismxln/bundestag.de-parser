# bundestag.de
## Initial commit (1.0.0)
<p> - parsing in 'a' tags persons href(links) and write them in persons_links.txt file (because sites don't like being hammered with requests)
(https://www.bundestag.de/en/members - Inspect - Network - XHR - File, open file, in this link find every profile(it is in <a> w/ title, href)). </p>
<p align='center'> <b> Now we can take links from persons_links.txt file. </p>
<h2>Parser check (1.0.1)</h2> 
<p> checking parser on name and company (i dont checking from file because parsing 700+ links vs just 1 link)</p>
<h2>Ready parser (1.0.2)</h2>
<p>We can stop here, but no, we can't. Site is blocking from frequent requests, let's iterations make randomly slow(next tag). Aaaand mine .select, dict is wrong...</p>
<h2>Its working, but slow! (1.0.3)</h2>
