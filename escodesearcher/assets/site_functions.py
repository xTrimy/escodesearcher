try:
    import html2text
except ImportError:
    print("No module named 'html2text' found")
    exit(0)


site_functions = {
    "www.geeksforgeeks.org":"geeks_for_geeks",
    "www.cplusplus.com":"cplusplus",
    # "www.stackoverflow.com",
    "www.tutorialspoint.com":"tutorialspoint",
    "www.programiz.com":"programiz",
}


class Functions:
    def __init__(self):
        super().__init__
        self.h = html2text.HTML2Text()
        self.h.ignore_links = True
        self.h.mark_code = False
        self.h.escape_all = True
        self.h.ignore_emphasis = True
        self.h.ul_item_mark = ""  # covered in cli
        self.h.emphasis_mark = ""  # covered in cli
        self.h.strong_mark = ""
        self.h.single_line_break = True

    def geeks_for_geeks(self, html_page):
        #TODO: Get file type (.cpp, .py, .java, ...)
        code_blocks = list(
            map(lambda x: self.h.handle(str(x)).replace(
                '`', ''), html_page.select(".code-block"))
        )
        return code_blocks

    def cplusplus(self, html_page):
        #TODO: Get file type (.cpp, .py, .java, ...)
        code_blocks = list(
            map(lambda x: self.h.handle(str(x)).replace(
                '`', ''), html_page.select("pre"))
        )
        return code_blocks

    def tutorialspoint(self, html_page):
        #TODO: Get file type (.cpp, .py, .java, ...)
        code_blocks = list(
            map(lambda x: self.h.handle(str(x)).replace(
                '`', ''), html_page.select(".prettyprint"))
        )
        return code_blocks

    def programiz(self, html_page):
        #TODO: Get file type (.cpp, .py, .java, ...)
        code_blocks = list(
            map(lambda x: self.h.handle(str(x)).replace(
                '`', ''), html_page.select("pre.exec"))
        )
        return code_blocks

