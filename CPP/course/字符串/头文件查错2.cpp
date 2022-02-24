#include <iostream>
#include "my Header.h"

using namespace std;

int main(){
   string header, read_header="";
    getline(cin, header);

    int index;      // 处理到: #include<
    for(index=0;index<header.size();index++){
        if (header[index]!=' '){
            read_header += header[index];
            if (header[index]=='<')
                break;
        }
    }
    // 把第一个: > 后面的非空字符全部加起来
    for( ; index<header.size();index++){
        if(header[index]=='>')
            for(; index < header.size();index++)
                if (header[index]!=' ')
                    read_header += header[index];
    }


    if (read_header != "#include<>"){
        cout << "include命令错误: "<<read_header<<endl;
        return 0;
    }
    else{
        cout << "导入成功！" << endl;
    }
}