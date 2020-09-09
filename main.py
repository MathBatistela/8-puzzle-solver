import puzzle as p
import sys

def write_file(result_list):
    output = open('output.txt','w')
    for level in result_list:
        output.write("-----------------------------------------------------------------------\n\n")
        output.write(f"Order: #{str(level[0].expansion_order)}\n")
        output.write(str(level[0]) + "\n")
        output.write("Expansions: \n\n")
        for exp in level[1]:
            output.write(str(exp) + "\n")
        output.write("-----------------------------------------------------------------------\n")
    output.close()
    
def print_terminal(result_list):
    for level in result_list:
        print("-----------------------------------------------------------------------")
        print(f"Order: #{level[0].expansion_order}")
        print(level[0])
        print("Expansions----")
        for exp in level[1]:
            print(exp)
        print("-----------------------------------------------------------------------")
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("modo de execução: python3 main.py [estado inicial] [vizualização (--terminal, --file, --all) ]")
        sys.exit(1)
        
    board = p.Puzzle(list([int(x) for x in sys.argv[1].split(',')]))
    result_list = board.solve()
    
    visu_param = sys.argv[2]   
     
    if visu_param == "--terminal":
        print_terminal(result_list)
    elif visu_param == "--file":
        write_file(result_list)
    elif visu_param == "--all":
        print_terminal(result_list)
        write_file(result_list)
        
    
