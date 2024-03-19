package com.romm.setlist.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Entity
@NoArgsConstructor @AllArgsConstructor @Setter @Getter @ToString @EqualsAndHashCode
public class Setlist {

    @Id @GeneratedValue
    private Long id;

    private String title;

    @OneToMany
    private Group group;
}
