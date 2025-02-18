from re import findall

class HandbookLexer():
    def lexRawString(self, raw_string:str):
        groups_raw = findall("(.)(\w*)(.)", raw_string)
        groups_stitch = []
        for group in groups_raw:
            stitched = []
            if group[0].isalpha():
                stitched.append(f"{group[0]}{group[1]}{group[2]}")
            else:
                stitched.append(group[0])
                stitched.append(group[1])
                stitched.append(group[2])
            groups_stitch.append(stitched)
        print(groups_stitch)
    
