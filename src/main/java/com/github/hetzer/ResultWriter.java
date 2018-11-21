package com.github.hetzer;

import java.io.PrintWriter;
import java.util.Arrays;

import com.github.sufbo.entities.java.Bytecode;
import com.github.sufbo.entities.java.ClassName;
import com.github.sufbo.entities.java.MethodInformation;
import com.github.sufbo.extractor.result.CsvResultWriter;

public class ResultWriter extends CsvResultWriter{
    private PrintWriter out;
    // private MethodRecommender methodRecommender = new MethodRecommender();

    public ResultWriter(PrintWriter out){
        super(out);
        this.out = out;
    }

    @Override
    public void visit(ClassName name, MethodInformation method, Bytecode bytecode) {
        print(name, "#", method);
        // print("\t->\t");
        // print(bytecode.length());
        // print(",", method.descriptor());
        print(",", bytecode.toString());
        // bytecode.buffer().toKGrams(2).intStream().forEach(a -> print(String.valueOf(","+a)));
        // print(",", method.start(), ",", method.end());
        out.println();
    }

    private void print(Object... objects){
        Arrays.stream(objects)
        .forEach(object -> print(String.valueOf(object)));
    }

    private void print(String value){
        out.print(value);
        // out.print(",");
    }
}
