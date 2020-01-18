def copy_template():
    with open("./templates/results_template.html", 'r') as original:
        contents = original.read().split("\n");
        with open("./templates/results.html", 'w') as new:
            for c in contents:
                new.write(c)


def copy_results(res):
    with open("./templates/results.html", 'a') as file:
        for item in res:
            title = item['title']
            string = "<a href='{0}'>{1}</a> <br/><br/>".format(item['link'], title)
            file.write(string+"\n")

        file.write("</div>\n</body>\n</html>")
