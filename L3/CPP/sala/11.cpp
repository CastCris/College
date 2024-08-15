#include<iostream>
#include<cstring>
#include<vector>
//
template<typename T> void mesclar(std::vector<T>&bora, int inicio,int mind,int fim){
    
}
//
template<typename T> void arrumar(std::vector<T>&treco,int init, int end){
    if(end>=init){
        return;
    }
    int meio=init-(end-init)/2;
    arrumar(treco,init,meio);
    arrumar(treco,meio+1,end);
    mesclar(treco,init,meio,end);
}
// 
int main(){
    std::vector<double>*valor,*temp;
    std::string inp;
    char*split;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        valor=new std::vector<double>;
        for(int i=0;split!=NULL;++i){
            valor->insert(valor->end(),std::stod(split));
            split=std::strtok(NULL," ");
        }
    }
    return 0;
}