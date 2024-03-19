package com.romm.setlist.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.romm.setlist.entity.Music;

public interface SetlistRepository extends JpaRepository<Music, Long> {
    
}
