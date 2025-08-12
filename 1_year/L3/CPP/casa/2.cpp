#include<iostream>
#include<cstring>
#include<vector>
#include"../bi.cpp"
//
int main(){
    std::string inp;
    std::vector<std::string>*treco;
    int v[4],*aux,temp,e;
    char*split;
    bool mudar;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=std::atoi(split);
            split=std::strtok(NULL," ");
        }
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            mudar=true;
            aux=new int(v[1]+v[0]);
        }
        e=v[0];
        treco=new std::vector<std::string>;
        treco->reserve((v[1]-v[0])/v[3]+1);
        while(e<=v[1]){
            (mudar)?temp=*aux-e:temp=e;
            if(temp%v[3]==0){
                treco->insert(treco->end(),std::to_string(temp));
            }
            e+=v[2];
        }
        std::cout<<"Numeros divisiveis por "<<v[3]<<": ";
        for(const std::string trem:*treco){
            std::cout<<trem<<" ";
        }
        std::cout<<std::endl;
        delete treco;
        treco=NULL;
        if(mudar){
            delete aux;
            aux=NULL;
        }
    }
    std::cout<<conver("Ta doido, nao vou utilizar o while()",34);
    return 0;
}