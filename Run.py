import sys
import inputANDoutput
import DataBase


if __name__ == "__main__":
    DataBase.Data_Base.creator_of_classes()
    inputANDoutput.InputAoutput.input_output()
    print(inputANDoutput.InputAoutput.main_list)
    sys.exit()

