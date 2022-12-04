<?php

class Section {
    public $start;
    public $end;

    function __construct($start, $end) {
        $this->start = $start;
        $this->end = $end;
    }
}

function parse_sections($input) {
    $sections = array();

    $s = explode(",", $input);

    foreach($s as $i) {
        $values = explode("-", $i);
        $sections[] = new Section(intval($values[0]), intval($values[1]));
    }

    return $sections;
}

function are_section_fully_overlapped_v1($sections) {
    if ($sections[0]->start >= $sections[1]->start && $sections[0]->end <= $sections[1]->end ||
        $sections[1]->start >= $sections[0]->start && $sections[1]->end <= $sections[0]->end) {
        return True;
    }
    return False;
}

function are_section_fully_overlapped_v2($sections) {
    $diff_start = $sections[0]->start - $sections[1]->start;
    $diff_end = $sections[0]->end - $sections[1]->end;

    if ($diff_start == 0 || $diff_end == 0) {
        return True;
    }
        
    if ($diff_start < 0 && $diff_end > 0 || $diff_start > 0 && $diff_end < 0) {
        return True;
    }

    return False;
}

function are_section_partially_overlapping_v1($sections) {
    if ($sections[0]->start > $sections[1]->end ||
        $sections[0]->end < $sections[1]->start ||
        $sections[1]->start > $sections[0]->end ||
        $sections[1]->end < $sections[0]->start) {
        return False;
    }
    return True;
}

function are_section_partially_overlapping_v2($sections) {
    $diff_1 = $sections[0]->end - $sections[1]->start;
    $diff_2 = $sections[1]->end - $sections[0]->start;

    if ($diff_1 >= 0 && $diff_2 >= 0) {
        return True;
    }
    return False;
}

$args = getopt("", ["input:"]);

if(isset($args["input"])) {
    $total_full_overlaps_v1 = 0;
    $total_partial_overlaps_v1 = 0;

    $total_full_overlaps_v2 = 0;
    $total_partial_overlaps_v2 = 0;

    $handle = fopen($args["input"], "r");

    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            $sections = parse_sections($line);

            if (are_section_fully_overlapped_v1($sections)) {
                $total_full_overlaps_v1 += 1;
            }

            if (are_section_partially_overlapping_v1($sections)) {
                $total_partial_overlaps_v1 += 1;
            }

            if (are_section_fully_overlapped_v2($sections)) {
                $total_full_overlaps_v2 += 1;
            }

            if (are_section_partially_overlapping_v2($sections)) {
                $total_partial_overlaps_v2 += 1;
            }
        }
        fclose($handle);
    }

    print("V1: Total full overlaps: " . $total_full_overlaps_v1 . " total partial overlap: " . $total_partial_overlaps_v1 . " \n");
    print("V2: Total full overlaps: " . $total_full_overlaps_v2 . " total partial overlap: " . $total_partial_overlaps_v2 . " \n");
} else {
    print_r("Supply input file with arg: --input <file path>\n");
}

?>