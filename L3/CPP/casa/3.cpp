#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include"../bi.cpp"
//
int main(){
    std::vector<std::vector<std::string>>*par;
    std::string inp;
    char*split;
    int v[4],*aux,mani,e;
    bool ok;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=atoi(split);
            split=std::strtok(NULL," ");
        }
        ok=false;
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]=v[1]-v[0];
            v[1]-=v[0];
            aux=new int(v[1]+v[0]);
            ok=true;
        }
        e=v[0];
        par=new std::vector<std::vector<std::string>>;
        par->resize(2);
        par->operator[](0).reserve((v[1]-v[0])/(v[3]*v[2])+1);
        par->operator[](1).reserve((v[1]-v[0]));
        while(e<=v[1]){
            (ok)?mani=*aux-e:mani=e;
            (mani%v[3]==0)?par->operator[](0).insert(par->operator[](0).end(),std::to_string(mani)):par->operator[](1).insert(par->operator[](1).end(),std::to_string(mani));
            e+=v[2];
        }
        std::cout<<"Numeros divisiveis por "<<v[3]<<": ";
        for(int i=0;i<par->operator[](0).size();++i){
            std::cout<<par->operator[](0)[i]<<" ";
        }
        std::cout<<"\nNumeros nao divisiveis por "<<v[3]<<": ";
        for(int i=0;i<par->operator[](1).size();++i){
            std::cout<<par->operator[](1)[i]<<" ";
        }
        std::cout<<std::endl;
        delete par;
        if(ok){
            delete aux;
            aux=NULL;
        }
        par=NULL;
        inp.clear();
    }
    std::cout<<conver("Ariba!",20);
    return 0;
}