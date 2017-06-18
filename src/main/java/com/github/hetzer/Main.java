package com.github.hetzer;

import java.util.stream.Stream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.PrintWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

import com.github.sufbo.entities.maven.Ids;
import com.github.sufbo.entities.maven.Artifact;
import com.github.sufbo.entities.maven.Artifacts;

// import com.github.hetzer.ArtifactStreamBuilder;

public class Main{
    private Artifacts artifacts;
    private Ids ids = new DummyIds().create();

    Main(String[] files){
        artifacts = new Artifacts(Stream.of(files)
            .map(path -> Paths.get(path))
            .map(path -> new Artifact(ids, path)));
    }

    private void run() throws IOException{
        try(PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out))){
            ResultWriter writer = new ResultWriter(out);
            artifacts.accept(writer);
        }
    }

    public static void main(String[] args) throws IOException{
        new Main(args).run();
    }
}
