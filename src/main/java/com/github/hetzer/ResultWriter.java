package com.github.hetzer;

import java.io.PrintWriter;
import java.util.Arrays;

import com.github.sufbo.entities.java.Bytecode;
import com.github.sufbo.entities.java.ClassName;
import com.github.sufbo.entities.java.MethodInformation;
import com.github.sufbo.extractor.result.CsvResultWriter;

public class ResultWriter extends CsvResultWriter{
    private PrintWriter out;

    public ResultWriter(PrintWriter out){
        super(out);
        this.out = out;
    }

    @Override
    public void visit(ClassName name, MethodInformation method, Bytecode bytecode) {
        print(name, "#", method);
        print(",", bytecode.toString());
        out.println();
    }

    private void print(Object... objects){
        Arrays.stream(objects)
        .forEach(object -> print(String.valueOf(object)));
    }

    private void print(String value){
        out.print(value);
    }
}
