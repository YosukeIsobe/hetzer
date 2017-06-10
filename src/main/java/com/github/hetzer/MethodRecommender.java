package com.github.hetzer;

import com.github.sufbo.entities.java.Bytecode;

public class MethodRecommender{
    private Bytecode bytecode;

    public MethodRecommender(Bytecode bytecode){
        this.bytecode = bytecode;
    }

    public Bytecode recommend(){
        // Pythonと連携してメソッド名を返す．
        return bytecode;
    }
}
