package com.github.hetzer;

import com.github.sufbo.entities.maven.Ids;
import com.github.sufbo.entities.maven.GroupId;
import com.github.sufbo.entities.maven.ArtifactId;
import com.github.sufbo.entities.maven.Version;

public class DummyIds{
    public Ids create(){
        return new Ids(new GroupId(""), new ArtifactId(""), new Version(""));
    }
}
