# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    working_dir = "calculator"
    # Tests for get file info
    # root_contents =  get_files_info(working_dir)
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "../")
    # print(pkg_contents)

    # Tests for get file content
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))

    # Tests to write file content
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum\n"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet\n"))
    print(write_file("calculator", "pkg2/morelorem.txt", "lorem ipsum dolor sit amet\n"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed\n"))

main()