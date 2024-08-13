#include<iostream>
#include<cstring>
#include<vector>
#include"../bi.cpp"
//
int main(){
    std::vector<std::vector<std::string>>*epa;
    std::string inp;
    char*split;
    int v[4],temp,*aux,*choice,direcionar;
    bool mudar;
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
        mudar=false;
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            aux=new int(v[0]+v[1]);
            mudar=true;
        }
        temp=0;
        epa=new std::vector<std::vector<std::string>>;
        epa->resize(2)        ;
        epa->operator[](0).reserve((v[1]-v[0])/v[3]+1);
        epa->operator[](1).reserve(v[1]-v[0]);
        choice=new int(v[0]);
        temp=v[0];
        do{
            direcionar=temp;
            if(mudar){
                ((*aux-temp)%v[3]==0)?*choice=0:*choice=1;
                direcionar=*aux-temp;
            } else if(temp%v[3]==0){
                *choice=0;
            } else{
                *choice=1;
            }
            epa->operator[](*choice).insert(epa->operator[](*choice).end(),std::to_string(direcionar));
            temp+=v[2];
        }while(temp-v[2]<v[1]);
        for(int i=0;i<2;++i){
            std::cout<<"Numeros";
            if(i==1){
                std::cout<<" nao";
            }
            std::cout<<" divisiveis por "<<v[3]<<": ";
            for(const std::string prin:epa->operator[](i)){
                std::cout<<prin<<" ";
            }
            std::cout<<std::endl;
        }
        delete epa;
        epa=NULL;
        if(mudar){
            delete aux;
            aux=NULL;
        }
        delete choice;
        choice=NULL;
    }
    std::cout<<conver("Bye, bye!",2)<<std::endl;
    return 0;
}