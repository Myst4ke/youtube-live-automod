:- dynamic not_toxic_message/0, very_toxic_message/0, threat_message/0, obscene_message/0, toxic_message/0, not_very_toxic_message/0, positive_message/0, negative_message/0, neutral_message/0, negative_high_intensity_emotion/0, negative_low_intensity_emotion/0, neutral_or_positive_emotion/0, repeated_offense/0.

/**** No toxic message *****/
rule(r1, action(do_nothing), []) :- not_toxic_message.

/**** Very toxic message *****/
rule(r2, action(ban_user), []) :- very_toxic_message.
rule(r3, action(sanction_level_three), []) :- very_toxic_message.

%Preference : sanction_level_three
rule(p1, prefer(r3, r2), []).

rule(p2, prefer(r2, r3), []) :- repeated_offense.
rule(c1, prefer(p2, p1), []) :- repeated_offense.

/**** Toxic message *****/
rule(r4, action(sanction_level_one), []) :- toxic_message.
rule(r5, action(sanction_level_two), []) :- toxic_message.
rule(r6, action(warning), []) :- toxic_message.
rule(r7, action(do_nothing), []) :- toxic_message.
rule(r99, action(sanction_level_three), []) :- toxic_message.

%Preference : warning
rule(p3, prefer(r6, r4), []).
rule(p4, prefer(r6, r5), []).
rule(p5, prefer(r6, r7), []).
rule(p98, prefer(r6, r99), []).

/********** Sentiment Analysis = Positive **********/
rule(p6, prefer(r7, r6), []) :- toxic_message, positive_message.
rule(c4, prefer(p6, p5), []) :- toxic_message, positive_message.

rule(p7, prefer(r6, r7), []) :- toxic_message, positive_message, negative_low_intensity_emotion.
rule(c5, prefer(p7, p6), []) :- toxic_message, positive_message, negative_low_intensity_emotion.

rule(p8, prefer(r4, r6), []) :- toxic_message, positive_message, negative_high_intensity_emotion.
rule(c6, prefer(p8, p3), []) :- toxic_message, positive_message, negative_high_intensity_emotion.

rule(p9, prefer(r4, r6), []) :- toxic_message, positive_message, negative_low_intensity_emotion, repeated_offense.
rule(c7, prefer(p9, p3), []) :- toxic_message, positive_message, negative_low_intensity_emotion, repeated_offense.

rule(p10, prefer(r5, r6), []) :- toxic_message, positive_message, negative_high_intensity_emotion, repeated_offense.
rule(c8, prefer(p10, c6), []) :- toxic_message, positive_message, negative_high_intensity_emotion, repeated_offense.

/********** Sentiment Analysis = Neutral **********/
rule(p11, prefer(r7, r6), []) :- toxic_message, neutral_message.
rule(c9, prefer(p11, p5), []) :- toxic_message, neutral_message.

rule(p12, prefer(r6, r7), []) :- toxic_message, neutral_message, negative_low_intensity_emotion.
rule(c10, prefer(p12, p11), []) :- toxic_message, neutral_message, negative_low_intensity_emotion.

rule(p13, prefer(r4, r6), []) :- toxic_message, neutral_message, negative_high_intensity_emotion.
rule(c11, prefer(p13, p3), []) :- toxic_message, neutral_message, negative_high_intensity_emotion.

rule(p14, prefer(r4, r6), []) :- toxic_message, neutral_message, negative_low_intensity_emotion, repeated_offense.
rule(c12, prefer(p14, p3), []) :- toxic_message, neutral_message, negative_low_intensity_emotion, repeated_offense.

rule(p15, prefer(r5, r6), []) :- toxic_message, neutral_message, negative_high_intensity_emotion, repeated_offense.
rule(c13, prefer(p15, c11), []) :- toxic_message, neutral_message, negative_high_intensity_emotion, repeated_offense.

/********** Sentiment Analysis = Negative **********/
rule(p16, prefer(r4, r6), []) :- toxic_message, negative_message.
rule(c14, prefer(p16, p3), []) :- toxic_message, negative_message.

rule(p17, prefer(r5, r6), []) :- toxic_message, negative_message, negative_high_intensity_emotion.
rule(c15, prefer(p17, c14), []) :- toxic_message, negative_message, negative_high_intensity_emotion.

rule(p18, prefer(r5, r6), []) :- toxic_message, negative_message, negative_low_intensity_emotion, repeated_offense.
rule(c16, prefer(p18, c14), []) :- toxic_message, negative_message, negative_low_intensity_emotion, repeated_offense.

rule(p19, prefer(r99, r6), []) :- toxic_message, negative_message, negative_high_intensity_emotion, repeated_offense.
rule(c17, prefer(p19, p98), []) :- toxic_message, negative_message, negative_high_intensity_emotion, repeated_offense.
rule(c18, prefer(p19, p17), []) :- toxic_message, negative_message, negative_high_intensity_emotion, repeated_offense.

/********** Complements **********/
complement(action(do_nothing), action(ban_user)).
complement(action(ban_user), action(do_nothing)).
complement(action(do_nothing), action(warning)).
complement(action(warning), action(do_nothing)).
complement(action(do_nothing), action(sanction_level_one)).
complement(action(sanction_level_one), action(do_nothing)).
complement(action(do_nothing), action(sanction_level_two)).
complement(action(sanction_level_two), action(do_nothing)).
complement(action(do_nothing), action(sanction_level_three)).
complement(action(sanction_level_three), action(do_nothing)).
complement(action(ban_user), action(warning)).
complement(action(warning), action(ban_user)).
complement(action(ban_user), action(sanction_level_one)).
complement(action(sanction_level_one), action(ban_user)).
complement(action(ban_user), action(sanction_level_two)).
complement(action(sanction_level_two), action(ban_user)).
complement(action(ban_user), action(sanction_level_three)).
complement(action(sanction_level_three), action(ban_user)).
complement(action(sanction_level_one), action(sanction_level_two)).
complement(action(sanction_level_two), action(sanction_level_one)).
complement(action(sanction_level_one), action(sanction_level_three)).
complement(action(sanction_level_three), action(sanction_level_one)).
complement(action(sanction_level_two), action(sanction_level_three)).
complement(action(sanction_level_three), action(sanction_level_two)).
complement(action(sanction_level_one), action(warning)).
complement(action(warning), action(sanction_level_two)).
complement(action(warning), action(sanction_level_three)).
complement(action(sanction_level_three), action(warning)).
complement(action(sanction_level_two), action(warning)).
complement(action(warning), action(sanction_level_two)).
