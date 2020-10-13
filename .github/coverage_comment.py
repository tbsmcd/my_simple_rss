import os


def create_comment():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cov_file = base_dir + '/cov.txt'
    with open(cov_file) as f:
        lines = f.readlines()
        coverage = ''
        for line in lines:
            line = line.strip()
            if line.startswith('TOTAL ') and line.endswith('%'):
                coverage = line
        coverage = coverage.split()[3]
        txt = ''.join(lines)
        comment = """
## Pytest coverage
**Coverage: {cov}**
            
<details>
{txt}
</details> 
        """.format(cov=coverage, txt=txt)
        print(comment)


if __name__ == '__main__':
    create_comment()
