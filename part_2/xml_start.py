import xml.dom.minidom

doc = xml.dom.minidom.parse("samplexml.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)


authors = doc.getElementsByTagName("author")
for author in authors:
    print(author.firstChild.data)


# new_skill = doc.createElement("author")
# new_skill.setAttribute("book", "New Book")
# doc.firstChild.appendChild(new_skill)
