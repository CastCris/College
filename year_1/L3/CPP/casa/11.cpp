#include<iostream>
#include<cstring>
#include "../bi.cpp"
//
int main(){
    std::string inp;
    char*split,*slot;
    double v[3];
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        std::cout<<"Tabuada de "<<v[1]<<" ate "<<v[2]<<" do numero "<<v[0]<<std::endl;
        for(double i=v[1];i<=v[2];i++){
            std::cout<<v[0]<<"."<<i<<" = "<<v[0]*i<<std::endl;
        }
    }
    std::cout<<conver("We are champions",17);
    return 0;
}