
def check(MainMatrix,SubMatix):
    #print(SubMatix)
    submatrix_hash = hash(str(SubMatix))
    main_col=len(MainMatrix[0])
    main_row=len(MainMatrix)
    sub_row=len(SubMatix)
    sub_col=len(SubMatix[0])
    #print(submatrix_hash)
    if sub_row>main_row and sub_col>main_col:
        print("No")
    else:
        hash_list = []
        for i in range(main_row - sub_row + 1):
            for j in range(main_col - sub_col + 1):
                for k in range(sub_row):
                    for l in range(sub_col):
                        SubMatix[k][l] = MainMatrix[i + k][j + l]
                #print(SubMatix)
                hash_list.append(hash(str(SubMatix)))
        if submatrix_hash in hash_list:
            print("Yes")
        else:
            print("No")

def GenrateMatrix(row,col):
    temp_matrix=[[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            temp_matrix[i][j] = int(input("Enter Matrix [" + str(i) + "][" + str(j) + "] elemnt:-"))
    return  temp_matrix

main_row,main_col=list(map(int,input("Enter Main Matrix Row and Colume with space exm 2 3 :- ").split()))
sub_row,sub_col=list(map(int,input("Enter Sub Matrix Row and Colume with space exm 2 3 :- ").split()))
if main_row<sub_row or main_col<sub_col:
    print("No")
else:
    print("Main Matrix")
    MainMatrix=GenrateMatrix(main_row,main_col)
    print("Sub Matrix")
    SubMatix=GenrateMatrix(sub_row,sub_col)
    check(MainMatrix,SubMatix)


