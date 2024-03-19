package com.romm.setlist.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.romm.setlist.entity.Group;

public interface GroupRepository extends JpaRepository<Group, Long> {
    
}
