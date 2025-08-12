#include<iostream>
#include<cstring>
#include<vector>
//
int main(){
    std::vector<int>*indexs;
    std::string inp,*nova;
    char*split,*slot,*temp;
    double ope,*num;
    bool outro;
    int e;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        nova=new std::string;
        nova->swap(inp);
        indexs=new std::vector<int>;
        indexs->reserve(nova->size()/2);
        for(int i=0;i<nova->length();++i){
            if(nova->operator[](i)=='*'|nova->operator[](i)=='/'){
                indexs->insert(indexs->end(),i);
            }
        }
        temp=new char[nova->size()];
        num=new double[2];
        for(const int iterar:*indexs){
            e=0;
            for(int i=iterar;nova->operator[](i)>46&&nova->operator[](i)<59;--i){
                temp[e]=nova->operator[](i);
                ++e;
            }
            num[0]=strtod(temp,&slot);
            for(int  i=0;i<e;++i){
                temp[i]='_';
            }
            e=0;
            for(int i=iterar;nova->operator[](i)>46&&nova->operator[](i)<59;++i){
                temp[e]=nova->operator[](i);
                ++e;
            }
            num[1]=strtod(temp,&slot);
            for(int  i=0;i<e;++i){
                temp[i]='_';
            }
            if(nova->operator[](iterar)=='*'){
                
            } else if(nova->operator[](iterar)=='/'){

            }
        }
        for(;nova->length()>0;){
            
        }
    }
    return 0;
}